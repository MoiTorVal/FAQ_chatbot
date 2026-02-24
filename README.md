# FAQ Chatbot — Amazon Electronics Q&A

A conversational FAQ chatbot built with Python, LangChain, ChromaDB, and Llama 3 via Ollama. The chatbot answers user questions about Amazon Electronics products using a dataset of real customer Q&A pairs.

---

## Tech Stack

- **Python 3.13**
- **LangChain** — prompt management and LLM chaining
- **Ollama + Llama 3** — local LLM for generating responses
- **ChromaDB** — vector store for semantic search
- **Pandas** — data loading and filtering
- **KaggleHub** — automatic dataset downloading

---

## Project Structure

```
FAQ_Chatbot/
├── src/
│   ├── data_loader.py      # Downloads and filters dataset
│   ├── embeddings.py       # Builds ChromaDB vector store
│   └── chatbot.py          # LangChain + Ollama chatbot logic
├── data/                   # Auto generated, not included in repo
├── main.py                 # Entry point
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### Step 1 — Clone the repository

```
git clone <your-repo-url>
cd FAQ_Chatbot
```

### Step 2 — Create and activate virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```
.venv\Scripts\activate
```

### Step 3 — Install dependencies

```
pip install -r requirements.txt
```

### Step 4 — Set up Kaggle API credentials

- Go to kaggle.com and log into your account
- Click your profile picture → Settings → API → Create New Token
- This downloads kaggle.json to your computer
- Move it to the following location:
  - Mac/Linux: ~/.kaggle/kaggle.json
  - Windows: C:\Users\YourUsername\.kaggle\kaggle.json

### Step 5 — Install and start Ollama

- Download Ollama from ollama.com
- Pull the Llama 3 model:

```
ollama pull llama3
```

- Ollama will start automatically in the background

### Step 6 — Run the chatbot

```
python main.py
```

---

## How It Works

1. **data_loader.py** downloads the Amazon Q&A dataset from Kaggle and filters it to 1,000 Electronics FAQ pairs
2. **embeddings.py** converts all FAQ questions into vectors and stores them in ChromaDB
3. When a user asks a question, ChromaDB searches for the most similar FAQ
4. The matching FAQ context is passed to Llama 3 to generate a natural response

---

## Dataset

Amazon Question and Answer Dataset

- Source: Kaggle
- Original data collected by Prof. Julian McAuley, UCSD
- 1.4 million Q&A pairs across 21 categories
- This project uses 1,000 Electronics category pairs

---

## Example Usage

```
You: Will this fit my iPad?
Bot: Yes, this product is compatible with the iPad.

You: Does this work with Samsung Galaxy?
Bot: Based on the FAQ, this product is compatible with Samsung Galaxy devices.
```

---

## Notes

- Do not delete the data/ folder between runs
- The first run will take longer as it downloads the dataset and builds the vector store
- Subsequent runs will be faster as the data is cached locally
