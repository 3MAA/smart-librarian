# 🤖 Smart Librarian – book recommendation chatbot

An intelligent chatbot that recommends books based on user queries, returns summaries, and can generate audio responses using TTS. The project includes:

- A database of 10 classic books with summaries (ChromaDB)
- Vector search using OpenAI (text-embedding-3-small)
- Text-to-Speech (TTS) with gTTS
- Speech-to-Text (STT)
- Profanity filter
- Backend and Frontend UI

---

## Features Implemented

- ✅ **Book summary database** (`book_summaries_dict`) – stores summaries for 10 titles.
- ✅ **Vector store** (Chroma + OpenAI embeddings) – used for semantic search in `search_books()`.
- ✅ **Chatbot API** – endpoint `/ask` receives user queries and returns a recommendation with summary.
- ✅ **Tool** `get_summary_by_title()` – fetches the full summary for a specific title.
- ✅ **Profanity filter** – implemented using `better_profanity`.
- ✅ **Backend + Frontend integration** – React UI and FastAPI backend.
- ✅ **Text-to-Speech (TTS)** – audio response generation using `gTTS`.
- ✅ **Speech-to-Text (STT)** – allows users to interact with the chatbot using voice. Speech input is transcribed using the Web Speech API and passed to the backend.

---

## Local installation

### Clone the project

```bash
git clone https://github.com/3MAA/smart-librarian.git
cd smart-librarian
```

### Frontend 

```bash
cd frontend
npm install
npm run dev
```

> Opens on: `http://localhost:5173`

---

### Backend 

```powershell
cd backend
python -m venv .venv
. .venv\Scripts\Activate.ps1
pip install -U pip
pip install -r requirements.txt

# Set your OpenAI API Key
setx OPENAI_API_KEY "sk-..."  # Replace with your actual API key

# Run the server
uvicorn main:app --reload --port 8000
```

> API available at: `http://localhost:8000/docs`

---

## Supported questions

| Question | Suggested book |
|------------------|----------------|
| Recommend me a novel about love and romance. | Pride and Prejudice |
| I’d like a book about the American Dream. | The Great Gatsby |
| Suggest me a fantasy and adventure book. | The Hobbit |
| Can you recommend me a book about war? | 1984 |

---

## Other questions

These questions trigger friendly fallback responses when no match is found:

- I couldn't find a relevant book in the current library. Could you provide more details?
- Do you know a book about parenting?
- Can you recommend a thriller book?
- I want a book about how to take care of cactus.

---

## Inappropriate language handling

If the user uses offensive or disrespectful language, the chatbot replies with:

> **Let's keep the conversation respectful. Please rephrase your request.**

Examples:

- “Books that aren't totally bullshit, please.”
- “Suggest a damn romance novel.”
- “I need a book with violence and revenge themes you stupid.”

---

## Technologies
| Component     | Technology              |
|---------------|--------------------------|
| Backend API   | Python, FastAPI, Uvicorn |
| Frontend UI   | React, Vite              |
| Vector Search | Chroma, OpenAI Embeddings|
| TTS           | gTTS                     |
| Profanity Filter | better_profanity     |
