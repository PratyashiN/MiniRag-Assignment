#  Construction RAG Chatbot

## Live Demo
LINK: https://minirag-assignment-muowjnyxtbhk6ceqfezc8g.streamlit.app/

---

##  Project Overview

This project implements a Retrieval-Augmented Generation (RAG) based chatbot that answers user queries using internal construction related documents.

Instead of relying on general knowledge, the system first retrieves relevant information from a set of documents and then generates responses strictly based on that context. This helps in reducing hallucination and ensures that answers remain grounded and reliable.

The application is deployed using Streamlit and provides an interactive interface where users can ask questions and view both the retrieved context and the generated response.

---

##  Model Choices

###  Embedding Model  
**Model Used:** `all-MiniLM-L6-v2` (Sentence Transformers)

This model was chosen because it is lightweight, fast, and performs well for semantic similarity tasks. Since the project requires converting both documents and user queries into vector representations for retrieval, this model provides a good balance between performance and efficiency.

---

###  LLM (Language Model)  
**Model Used:** LLaMA 3 (8B Instruct via OpenRouter)

LLaMA 3 was selected due to its strong ability to follow instructions and generate structured responses. Using OpenRouter made it easy to integrate the model through an API without requiring local deployment, which keeps the system efficient and easy to run.

---

##  Document Chunking & Processing

All documents are stored in a `data/` folder and are processed before being used in the system.

- Each document is divided into smaller chunks (around 300 characters)
- Chunking helps in:
  - Improving retrieval accuracy  
  - Preserving meaningful context  
  - Avoiding overly long inputs to the model  

These chunks are then used for embedding and retrieval.

---

##  Retrieval Mechanism (FAISS)

The project uses FAISS (Facebook AI Similarity Search) as a vector database.

### Steps:

1. Each chunk is converted into an embedding using the embedding model  
2. All embeddings are stored in a FAISS index  
3. When a user asks a question:
   - The query is converted into an embedding  
   - FAISS retrieves the most relevant chunks  
4. These chunks are then passed to the LLM  

This ensures that the model only sees the most relevant parts of the documents.

---

##  Grounded Answer Generation

One of the key goals of this project is to avoid hallucination.

To ensure this:

- The model is instructed to use only the retrieved context  
- External knowledge is restricted  
- The system allows only **simple, reasonable inference** when something is implied  

This makes the answers:
- More accurate  
- More trustworthy  
- Clearly tied to the source documents  

---

##  Frontend (Streamlit Interface)

The chatbot interface is built using Streamlit.

It provides:
- A simple input box for user queries  
- Display of retrieved document chunks  
- Generated answer section  

This transparency helps users understand **why a particular answer was generated**, which is an important aspect of RAG systems.

---

##  How to Run the Project Locally

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd rag-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Set your API key
Windows:
```bash
set OPENROUTER_API_KEY=your_api_key
```
Mac/Linux:
```bash
export OPENROUTER_API_KEY=your_api_key
```
### 4. Run the app
```bash
streamlit run app.py
 ```
5. Open in Browser

After running the command, the app will open automatically.
If not, open this in your browser:

http://localhost:8501

##  Quality Analysis

To evaluate the performance of the RAG system, a set of test questions was created based on the provided documents. These questions were designed to cover different aspects such as delay management, payments, transparency, and project tracking.
---
### Test Questions
The following questions were used for evaluation:
1. What factors affect construction project delays?  
2. How can construction delays be reduced?  
3. What is the role of an integrated project management system?  
4. How are contractor payments handled?  
5. What ensures accountability in construction projects?  
6. What is the purpose of escrow-based payments?  
7. How is transparency maintained in the construction process?  
8. How is project progress tracked?  
9. What is stage-based contractor payment?  
10. What are the key features of delay management and accountability?  
---
###  Evaluation Criteria
The system was evaluated based on the following criteria:
- **Relevance of retrieved chunks:** Whether the retrieved context matches the user query  
- **Groundedness:** Whether the generated answers are based only on retrieved context  
- **Hallucination:** Whether the model introduces unsupported or external information  
- **Clarity:** Whether the answers are clear, concise, and well-structured  
---
###  Observations
- The retrieved chunks were generally relevant to the user queries, indicating that the embedding model and FAISS based retrieval are effective.  
- The generated answers were mostly grounded in the retrieved context, with minimal use of external or unsupported information.  
- The system showed low hallucination, as it either stayed within the provided context or gave cautious responses when information was not explicitly available.  
- The answers were concise and structured, often presented in bullet points, making them easy to understand.  
- The system performed well for both direct questions (e.g., solutions to delays) and slightly inferential questions (e.g., factors affecting delays).  
---

###  Conclusion

Overall, the system demonstrates strong performance in retrieving relevant information and generating accurate, context-based answers. The prompt design ensures that responses remain grounded, while still allowing simple and reasonable inference when required. This results in a reliable and effective document-based question-answering system.
