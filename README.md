# AI Internal Knowledge Chatbot 🤖

A Retrieval-Augmented Generation (RAG) based chatbot developed for the **Teyzix Core AI Internship (AI-2 Task)**.
The chatbot intelligently retrieves information from internal company documents and generates contextual answers using Large Language Models (LLMs).

---

# 📌 Project Overview

Employees often spend significant time searching through company documents such as HR policies, onboarding manuals, and technical guides. This project solves that problem by building an AI-powered chatbot capable of retrieving relevant information from internal documents and answering employee queries accurately.

The system uses:

- **SentenceTransformers** for vector embeddings
- **FAISS** for vector storage and semantic retrieval
- **OpenRouter LLM API** for response generation
- **Streamlit** for interactive user interface

The chatbot answers questions strictly based on the provided internal documents.

---

# 🚀 Features

✅ Document ingestion pipeline
✅ Text chunking and preprocessing
✅ Semantic vector embeddings
✅ FAISS vector database integration
✅ Context-aware retrieval system
✅ LLM-powered answer generation
✅ Streamlit interactive UI
✅ Chat history support
✅ Source citations display
✅ Modular project architecture
✅ OpenRouter free-tier integration

---

# 🛠️ Technologies Used

| Technology               | Purpose                         |
| ------------------------ | ------------------------------- |
| Python 3.11              | Core programming language       |
| Streamlit                | Frontend user interface         |
| SentenceTransformers     | Embedding generation            |
| FAISS                    | Vector database                 |
| LangChain                | Document processing             |
| OpenRouter API           | LLM response generation         |
| HuggingFace Transformers | NLP support                     |
| dotenv                   | Environment variable management |

---

# 📂 Project Structure

```bash
AI-RAG-Chatbot/
│
├── sample_docs/
│   ├── hr_policy.txt
│   ├── onboarding_guide.txt
│   └── technical_wiki.txt
│
├── vector_store/
│
├── app.py
├── chatbot.py
├── ingestion.py
├── retrieval.py
├── vector_store.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# ⚙️ System Architecture

The chatbot follows a Retrieval-Augmented Generation (RAG) workflow:

1. Internal documents are loaded from the `sample_docs` folder.
2. Documents are split into smaller chunks.
3. Chunks are converted into vector embeddings using SentenceTransformers.
4. Embeddings are stored in FAISS vector database.
5. User queries are semantically matched against stored vectors.
6. Relevant document chunks are retrieved.
7. Retrieved context is combined with the user query.
8. OpenRouter LLM generates the final contextual response.
9. Response and source citations are displayed in Streamlit UI.

---

# 📥 Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone <your-github-repository-link>
cd AI-RAG-Chatbot
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

# 📄 Add Internal Documents

Place sample documents inside:

```bash
sample_docs/
```

Supported format currently:

- `.txt`

Example documents:

- HR policies
- Employee onboarding manuals
- Technical documentation

---

# 🧠 Create Vector Database

Run:

```bash
python vector_store.py
```

This will:

- load documents
- split text into chunks
- generate embeddings
- create FAISS vector database

---

# ▶️ Run Streamlit Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

# 💬 Example Questions

You can ask questions such as:

```text
What is the company leave policy?
```

```text
What are office timings?
```

```text
Is remote work allowed?
```

```text
What technologies are used by the development team?
```

---

# 📚 Source Citations

The chatbot includes source citation support.
It displays the document source used to generate each answer, improving transparency and explainability.

---

# 📸 Screenshots

## Chatbot Interface

(Add screenshot here)

## Query Handling

(Add screenshot here)

## Source Citations

(Add screenshot here)

## Streamlit Deployment

(Add screenshot here)

---

# 🌐 Deployment

The application is deployed using Streamlit Cloud.

## Live Demo

(Add deployment link here)

---

# 🎥 Demo Video

The demo video includes:

- Document ingestion process
- Vector database creation
- Query handling
- Retrieval process
- Response generation
- Streamlit UI walkthrough

---

# 📊 Future Improvements

Possible future enhancements include:

- PDF and DOCX support
- Multi-user authentication
- Conversation memory
- Voice input support
- Advanced citation highlighting
- Dark mode UI
- Docker deployment

---

# 🧪 Sample Internal Documents Used

The project uses sample company documents for testing:

- HR Policy
- Employee Onboarding Guide
- Technical Wiki

---

# 👨‍💻 Author

**Bisma Imran**
AI & Machine Learning Intern
Teyzix Core Internship Program

---
