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

##  Local LLM Comparison

As an additional exploration, a comparison was made between an API based LLM (LLaMA 3 via OpenRouter) and a local open source LLM.

---

###  Models Used

- **API-based Model:** LLaMA 3 (8B Instruct via OpenRouter)  
- **Local Model:** Phi-3 Mini (3.8B) 

---

###  Comparison

#### 1. Answer Quality  
The OpenRouter based LLaMA 3 model produced more accurate, detailed, and well structured responses. It followed instructions more effectively and generated clearer answers.  
In comparison, the local Phi-3 Mini model, due to its smaller size, may produce simpler responses and sometimes lacks depth in reasoning.

---

#### 2. Latency  
Local models can offer faster response times after initial setup since they run directly on the machine without requiring API calls.  
However, API-based models introduce slight latency due to network communication, although this was not significant for this project.

---

#### 3. Groundedness to Retrieved Context  
Both models rely on retrieved context for answering queries.  
However, LLaMA 3 demonstrated better adherence to prompt instructions, resulting in more consistent grounding and fewer chances of hallucination.  
Smaller local models may occasionally deviate slightly from the provided context.

---

#### 4. Ease of Setup and Use  
Using LLaMA 3 via OpenRouter was straightforward, requiring only an API key and minimal configuration.  
On the other hand, running a local model like Phi-3 Mini requires additional setup, including installing dependencies and ensuring sufficient system resources.

---

##  Conclusion

This project demonstrates the practical implementation of a Retrieval-Augmented Generation (RAG) system for building reliable and context aware AI applications. By combining semantic search with a language model, the chatbot is able to generate responses that are grounded in actual documents rather than relying on general knowledge.
The use of document chunking, vector embeddings, and FAISS based retrieval ensures that only relevant information is passed to the model, improving both accuracy and efficiency. Additionally, careful prompt design helps reduce hallucination and ensures that responses remain aligned with the provided context.
Through evaluation and testing, the system showed strong performance in retrieving relevant information and generating clear, structured answers. The deployment using Streamlit further demonstrates how such systems can be made accessible through simple and interactive interfaces.
Overall, this project highlights the effectiveness of RAG systems in real-world scenarios where accuracy, transparency, and reliability are important. It also provides a solid foundation for further improvements, such as enhancing retrieval strategies, integrating larger datasets, or experimenting with different language models.
