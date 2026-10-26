# FinWise AI: AI-Powered Personal Financial Analysis and Smart Budget Assistant

FinWise AI is an educational FinTech web application built using **Streamlit** and **LangChain**[cite: 17]. It combines deterministic financial calculations in Python with structured, educational AI insights powered by OpenAI (`gpt-4o-mini`)[cite: 18, 19, 20].

> ⚠️ **IMPORTANT - EDUCATIONAL USE ONLY:** This application is an educational prototype. It must not provide guaranteed investment advice, execute financial transactions, connect to real bank accounts, or claim that any financial outcome is guaranteed[cite: 17].

---

## 🚀 Features
- **Deterministic Financial Calculations:** Computes total expenses, remaining income, savings ratio, expense ratio, and a preliminary health score (0-100) locally in Python.
- **Structured AI Insights:** Leverages LangChain prompts and `ChatOpenAI` to return a strict JSON schema containing financial health scores, spending analysis, risk levels, and action plans.
- **Live Streaming Output:** Streams AI recommendations dynamically onto the user interface for a natural typing effect.
- **Flexible Caching:** Supports both **In-Memory (`InMemoryCache`)** and **Disk-based (`SQLiteCache`)** caching to optimize performance and reduce API costs.

---

## 📂 Project Folder Structure
```text
Fin Tech Ai/
│
├── app.py                  # Main Streamlit UI application
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables template
├── README.md               # Project documentation
└── src/
    ├── __init__.py
    ├── financial_calculator.py # Deterministic math logic
    ├── prompts.py              # System prompts & JSON schema templates
    ├── chains.py               # LangChain integration & streaming
    ├── cache_manager.py        # In-Memory & SQLite caching setup
    └── utils.py                # Safe JSON parsing helpers



🛠️ Setup and Installation Instructions
1. Clone the Repository:
git clone [https://github.com/Tabish-Niaz/fin-tech-ai.git](https://github.com/your-username/fin-tech-ai.git)

2. cd fin-tech-ai

3. Create a Virtual Environment (Python 3.10+ Recommended):
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

4. Install Dependencies:
pip install -r requirements.txt

5. Configure Environment Variables:
Copy the .env file to create a new file named .env:
cp .env .env
Open .env and add your OpenAI API key:
Code snippet :
OPENAI_API_KEY="sk-proj-your-api-key-here"

6. Run the Application:Bashstreamlit 
streamlit run app.py


🧠 Technical Architecture & Explanations
1. Python Calculations vs. AI Insights
Python Calculations (financial_calculator.py): 
All core mathematical operations (such as summing expenses, calculating percentages, and computing the preliminary health score) are performed deterministically in Python. This ensures absolute accuracy and consistency—the exact same inputs will always produce the exact same numerical outputs.   
AI Insights (chains.py & prompts.py): 
The LLM (gpt-4o-mini) does not perform raw math[cite: 19, 20]. Instead, it receives the pre-calculated metrics and financial goals dynamically through LangChain templates to generate contextual, qualitative, and educational budgeting recommendations structured in strict JSON[cite: 20].


2. Caching Implementation (cache_manager.py)
To prevent redundant API calls and optimize performance, FinWise AI integrates LangChain's global caching mechanism (set_llm_cache)[cite: 21]:
InMemoryCache: 
Stores responses temporarily in RAM. Best for single active sessions for ultra-fast retrieval[cite: 21].
SQLiteCache: 
Persists responses to a local .langchain_cache.db file on disk. This survives application restarts and is ideal for reusing cached insights across multiple sessions[cite: 21].