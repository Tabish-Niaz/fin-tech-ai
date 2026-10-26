from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

SYSTEM_PROMPT = """You are FinWise AI, an educational financial assistant.
IMPORTANT: Your advice is for informational purposes only. You must not provide guaranteed investment advice or execute transactions.
You must return ONLY a valid JSON object matching this exact structure:
{{
  "financial_summary": "string summary",
  "financial_health_score": 85,
  "spending_analysis": [
    {{"category": "category name", "observation": "observation text", "recommendation": "recommendation text"}}
  ],
  "risk_level": "LOW / MEDIUM / HIGH",
  "top_priorities": ["priority1", "priority2"],
  "budget_recommendations": ["rec1", "rec2"],
  "savings_strategy": ["strat1", "strat2"],
  "next_month_action_plan": ["action1", "action2"]
}}"""

HUMAN_PROMPT = """
User Financial Data:
- Monthly Income: {monthly_income}
- Total Expenses: {total_expenses}
- Remaining Income: {remaining_income}
- Current Savings: {savings}
- Savings Ratio: {savings_ratio}%
- Expense Ratio: {expense_ratio}%
- Financial Goal: {financial_goal}
- Expense Breakdown: {expense_breakdown}

Analyze the data and provide the exact JSON output.
"""

def get_prompt_template():
    return ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(SYSTEM_PROMPT),
        HumanMessagePromptTemplate.from_template(HUMAN_PROMPT)
    ])