import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from openai import OpenAI
import os

# -------------------------------
# CONFIG
# -------------------------------
st.set_page_config(page_title="Construction RAG Assistant")

st.title("Construction AI Assistant")
st.write("Ask questions based on internal documents.")

# -------------------------------
# LOAD MODEL
# -------------------------------
model = SentenceTransformer('all-MiniLM-L6-v2')

# -------------------------------
# LOAD DOCUMENTS
# -------------------------------
def load_docs():
    docs = []
    for file in os.listdir("data"):
        with open(f"data/{file}", "r", encoding="utf-8") as f:
            docs.append(f.read())
    return docs

# -------------------------------
# CHUNKING
# -------------------------------
def chunk_text(text, size=300):
    return [text[i:i+size] for i in range(0, len(text), size)]

# -------------------------------
# PREPARE DATA
# -------------------------------
@st.cache_resource
def prepare():
    docs = load_docs()

    chunks = []
    for d in docs:
        chunks.extend(chunk_text(d))

    embeddings = model.encode(chunks)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    return chunks, index

chunks, index = prepare()

# -------------------------------
# RETRIEVE
# -------------------------------
def retrieve(q, k=5):
    emb = model.encode([q])
    _, idx = index.search(emb, k)
    return [chunks[i] for i in idx[0]]

# -------------------------------
# LLM
# -------------------------------
client =  OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY") 
)

def generate(context, question):
    context_text = "\n\n".join(context)

    prompt = f"""
Answer the question using ONLY the context below.

- Do not use outside knowledge
- If needed, infer simple points from the context
- Keep answer short and in bullet points

Context:
{context_text}

Question:
{question}

Answer:
"""

    res = client.chat.completions.create(
        model="meta-llama/llama-3-8b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return res.choices[0].message.content

# -------------------------------
# UI
# -------------------------------
q = st.text_input("Ask a question")

if q:
    retrieved = retrieve(q)
    ans = generate(retrieved, q)

    st.subheader("Retrieved Context")
    for i, c in enumerate(retrieved):
        st.write(f"Chunk {i+1}: {c}")

    st.subheader(" Answer")
    st.write(ans)
