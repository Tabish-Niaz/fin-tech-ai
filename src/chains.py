from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate
from src.prompts import get_prompt_template

def get_financial_chain(api_key):
    # Yeh chain dashboard ko JSON dene ke liye hai
    llm = ChatOpenAI(temperature=0.2, model="gpt-4o-mini", openai_api_key=api_key)
    prompt = get_prompt_template()
    return prompt | llm

def stream_recommendations(api_key, inputs):
    # Yeh chain user ko screen par plain text dikhane ke liye hai
    llm = ChatOpenAI(temperature=0.2, model="gpt-4o-mini", openai_api_key=api_key, streaming=True)
    
    NARRATIVE_PROMPT = """You are FinWise AI, an expert financial assistant. 
    Write a short, friendly, and encouraging 3-sentence summary directly to the user based on these numbers:
    Income: {monthly_income}, Expenses: {total_expenses}, Remaining: {remaining_income}, Savings Ratio: {savings_ratio}%.
    IMPORTANT: Write in plain English. DO NOT use JSON format."""
    
    prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(NARRATIVE_PROMPT)
    ])
    
    messages = prompt.format_messages(**inputs)
    
    for chunk in llm.stream(messages):
        if chunk.content:
            yield chunk.content