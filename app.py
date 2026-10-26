# import streamlit as st
# import os
# from dotenv import load_dotenv
# from src.financial_calculator import calculate_financials
# from src.cache_manager import enable_caching
# from src.chains import get_financial_chain, stream_recommendations
# from src.utils import parse_json_safely

# # Load Environment Variables
# load_dotenv()
# API_KEY = os.getenv("OPENAI_API_KEY")

# st.set_page_config(page_title="FinWise AI", page_icon="💰", layout="wide")


# # Custom CSS for Neon/Cyberpunk Look
# st.markdown("""
# <style>
# /* Main App Background */
# .stApp {
#     background-color: #0b0f19;
#     color: #e6edf3;
# }

# /* Sidebar Styling */
# [data-testid="stSidebar"] {
#     background-color: #111827;
#     border-right: 1px solid #00f0ff;
#     box-shadow: 5px 0 20px rgba(0, 240, 255, 0.15);
# }

# /* Input Fields (Numbers, Dropdowns) with Glowing Cyan Borders */
# div[data-baseweb="input"] > div, 
# div[data-baseweb="select"] > div {
#     background-color: #0b0f19 !important;
#     border: 1px solid #00f0ff !important;
#     border-radius: 8px !important;
#     box-shadow: 0 0 8px rgba(0, 240, 255, 0.3) !important;
#     color: white !important;
# }

# /* Primary Button Styling (Analyze Finances) */
# button[kind="primary"] {
#     background: linear-gradient(90deg, #00f0ff 0%, #0055ff 100%) !important;
#     color: white !important;
#     border: none !important;
#     box-shadow: 0 0 15px rgba(0, 240, 255, 0.5) !important;
#     border-radius: 8px !important;
#     font-weight: bold !important;
#     transition: all 0.3s ease;
# }
# button[kind="primary"]:hover {
#     box-shadow: 0 0 25px rgba(0, 240, 255, 0.8) !important;
#     transform: scale(1.02);
# }

# /* Main Form Area Styling */
# div[data-testid="stForm"] {
#     border: 1px solid #00f0ff;
#     border-radius: 12px;
#     padding: 25px;
#     box-shadow: 0 0 20px rgba(0, 240, 255, 0.1);
#     background-color: #111827;
# }

# /* Red Disclaimer / Medical Notice Box */
# div.stAlert[data-baseweb="notification"] {
#     background-color: rgba(255, 75, 75, 0.1) !important;
#     border: 1px solid #ff4b4b !important;
#     color: #ff4b4b !important;
#     border-radius: 8px !important;
# }
# </style>
# """, unsafe_allow_html=True)

# # Educational Disclaimer
# DISCLAIMER = "⚠️ EDUCATIONAL PURPOSES ONLY: This application is an educational prototype. It does not provide guaranteed investment advice, execute financial transactions, or connect to real bank accounts. Please consult a qualified financial professional."

# with st.sidebar:
#     st.title("💰 FinWise AI")
#     st.error(DISCLAIMER)
    
#     st.subheader("Settings")
#     cache_option = st.selectbox("Caching System", ["None", "In-Memory", "SQLite"], index=2)
#     enable_caching(cache_option)
    
#     if st.button("Reset Session", use_container_width=True):
#         st.rerun()

# st.title("Personal Financial Analysis & Budget Assistant")
# st.warning(DISCLAIMER)

# # Form Inputs
# with st.form("finance_form"):
#     col1, col2 = st.columns(2)
#     with col1:
#         income = st.number_input("Monthly Income", min_value=0.0, value=5000.0)
#         savings = st.number_input("Current Monthly Savings", min_value=0.0, value=1000.0)
#         goal = st.selectbox("Financial Goal", ["Save money", "Emergency fund", "Pay off debt", "Vacation", "Start a business", "Improve budgeting"])
#         currency = st.selectbox("Currency", ["USD ($)", "PKR (Rs)", "EUR (€)", "GBP (£)"])
    
#     with col2:
#         st.markdown("**Monthly Expenses (10 Categories)**")
#         housing = st.number_input("Housing/Rent", min_value=0.0, value=1500.0)
#         food = st.number_input("Food", min_value=0.0, value=600.0)
#         transportation = st.number_input("Transportation", min_value=0.0, value=300.0)
#         utilities = st.number_input("Utilities", min_value=0.0, value=200.0)
#         education = st.number_input("Education", min_value=0.0, value=0.0)
#         healthcare = st.number_input("Healthcare", min_value=0.0, value=150.0)
#         entertainment = st.number_input("Entertainment", min_value=0.0, value=200.0)
#         debt = st.number_input("Loan/Debt", min_value=0.0, value=0.0)
#         other = st.number_input("Other", min_value=0.0, value=100.0)
        
#     submitted = st.form_submit_button("Analyze Finances", type="primary", use_container_width=True)

# if submitted:
#     if not API_KEY:
#         st.error("API Key is missing! Please add it to your .env file or Streamlit Secrets.")
#         st.stop()
        
#     expenses_dict = {
#         "Housing": housing, "Food": food, "Transportation": transportation, 
#         "Utilities": utilities, "Education": education, "Healthcare": healthcare, 
#         "Entertainment": entertainment, "Debt": debt, "Other": other
#     }
    
#     # Process Deterministic Calculations
#     metrics = calculate_financials(income, expenses_dict, savings)
    
#     st.divider()
#     st.subheader("📊 Financial Overview (Calculated)")
#     m1, m2, m3, m4 = st.columns(4)
#     m1.metric("Total Expenses", f"{metrics['total_expenses']:,.2f}")
#     m2.metric("Remaining Income", f"{metrics['remaining_income']:,.2f}")
#     m3.metric("Savings Ratio", f"{metrics['savings_ratio']}%")
#     m4.metric("Expense Ratio", f"{metrics['expense_ratio']}%")
    
#     st.progress(metrics['preliminary_score'] / 100.0, text=f"Preliminary Health Score: {metrics['preliminary_score']}/100")
    
#     inputs = {
#         "monthly_income": income,
#         "total_expenses": metrics['total_expenses'],
#         "remaining_income": metrics['remaining_income'],
#         "savings": savings,
#         "savings_ratio": metrics['savings_ratio'],
#         "expense_ratio": metrics['expense_ratio'],
#         "financial_goal": goal,
#         "expense_breakdown": str(expenses_dict)
#     }

#     st.markdown("### 🤖 AI Financial Analysis")
#     with st.chat_message("assistant"):
#         st.write_stream(stream_recommendations(API_KEY, inputs))
        
#     with st.spinner("Generating structured JSON insights..."):
#         chain = get_financial_chain(API_KEY)
#         raw_output = chain.invoke(inputs)
#         result = parse_json_safely(raw_output.content)
        
#         if result:
#             r_level = result.get("risk_level", "UNKNOWN").upper()
#             if "HIGH" in r_level: st.error(f"🚨 Risk Level: {r_level}")
#             elif "MEDIUM" in r_level: st.warning(f"⚠️ Risk Level: {r_level}")
#             else: st.success(f"🟢 Risk Level: {r_level}")
            
#             t1, t2, t3 = st.tabs(["Spending & Priorities", "Budget Strategy", "Next Actions"])
            
#             with t1:
#                 st.info(result.get("financial_summary", ""))
#                 st.markdown("**Spending Analysis**")
#                 for cat in result.get("spending_analysis", []):
#                     st.write(f"- **{cat.get('category')}**: {cat.get('observation')} ➔ *{cat.get('recommendation')}*")
#                 st.markdown("**Top Priorities**")
#                 for p in result.get("top_priorities", []): st.write(f"✔️ {p}")
                
#             with t2:
#                 st.markdown("**Budget Recommendations**")
#                 for b in result.get("budget_recommendations", []): st.write(f"- {b}")
#                 st.markdown("**Savings Strategy**")
#                 for s in result.get("savings_strategy", []): st.write(f"- {s}")
                
#             with t3:
#                 st.markdown("**Next Month Action Plan**")
#                 for a in result.get("next_month_action_plan", []): st.write(f"🎯 {a}")
#         else:
#             st.error("Failed to parse the AI JSON output. Please try again.")
#             st.code(raw_output.content)



import streamlit as st
import os
from dotenv import load_dotenv
from src.financial_calculator import calculate_financials
from src.cache_manager import enable_caching
from src.chains import get_financial_chain, stream_recommendations
from src.utils import parse_json_safely

# Load Environment Variables
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="FinWise AI", page_icon="💰", layout="wide")

# Streamlit ke default Header (Fork/GitHub) aur Footer ko hide karne ka CSS
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# ==========================================
# GLOWING NEON CSS (MediGuide Style applied to FinWise)
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] { 
        font-family: 'Inter', sans-serif !important; 
    }
    
    /* Radial Gradient Background */
    [data-testid="stAppViewContainer"] {
        background-image: radial-gradient(circle at 50% 0%, #0a1930 0%, #050b14 70%) !important;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: rgba(17, 24, 39, 0.8) !important;
        border-right: 1px solid #00F2FE;
        box-shadow: 5px 0 20px rgba(0, 242, 254, 0.15);
    }
    
    /* Glowing Inputs */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > div,
    .stTextArea > div > div > textarea,
    .stMultiSelect > div > div > div {
        background-color: rgba(10, 20, 36, 0.8) !important;
        border: 1px solid #00F2FE !important;
        border-radius: 8px !important;
        box-shadow: 0 0 10px rgba(0, 242, 254, 0.15) !important;
        color: white !important;
    }
    
    /* Form Background */
    [data-testid="stForm"] {
        background-color: transparent !important;
        border: none !important;
    }
    
    /* Glowing Cyan Button */
    div[data-testid="stFormSubmitButton"] > button, .stButton > button {
        background: linear-gradient(90deg, #00F2FE 0%, #4FACFE 100%) !important;
        color: #000000 !important;
        font-weight: 800 !important;
        font-size: 16px !important;
        border: none !important;
        border-radius: 8px !important;
        box-shadow: 0 0 20px rgba(0, 242, 254, 0.6) !important;
        transition: all 0.3s ease !important;
    }
    div[data-testid="stFormSubmitButton"] > button:hover, .stButton > button:hover {
        box-shadow: 0 0 30px rgba(0, 242, 254, 0.9) !important;
        transform: scale(1.02) !important;
    }
    
    /* Red Disclaimer / Medical Notice Box */
    div.stAlert[data-baseweb="notification"] {
        background-color: rgba(255, 75, 75, 0.1) !important;
        border: 1px solid #ff4b4b !important;
        color: #ff4b4b !important;
        border-radius: 8px !important;
    }
</style>
""", unsafe_allow_html=True)

# Educational Disclaimer
DISCLAIMER = "⚠️ **EDUCATIONAL PURPOSES ONLY:** This application is an educational prototype. It does not provide guaranteed investment advice, execute financial transactions, or connect to real bank accounts. Please consult a qualified financial professional."

with st.sidebar:
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 25px;">
        <div style="font-size: 28px;">💰</div>
        <h2 style="margin: 0; color: #00F2FE !important; font-weight: 800;">FinWise AI</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='font-size: 0.8rem; font-weight: 600; color: #E2E8F0; margin-bottom: 5px;'>Caching settings</p>", unsafe_allow_html=True)
    cache_option = st.selectbox("Caching System", ["None", "In-Memory", "SQLite"], index=2, label_visibility="collapsed")
    enable_caching(cache_option)
    
    if st.button("Reset Session", use_container_width=True):
        # Session state ki saari values clear kar ke app restart karne ke liye
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.error(DISCLAIMER)

st.markdown("<h1 style='color: white;'>Personal Financial Analysis & Budget Assistant</h1>", unsafe_allow_html=True)

# Form Inputs
with st.form("finance_form"):
    col1, col2 = st.columns(2)
    with col1:
        income = st.number_input("Monthly Income", min_value=0.0, value=5000.0)
        savings = st.number_input("Current Monthly Savings", min_value=0.0, value=1000.0)
        goal = st.selectbox("Financial Goal", ["Save money", "Emergency fund", "Pay off debt", "Vacation", "Start a business", "Improve budgeting"])
        currency = st.selectbox("Currency", ["USD ($)", "PKR (Rs)", "EUR (€)", "GBP (£)"])
    
    with col2:
        st.markdown("**Monthly Expenses (10 Categories)**")
        housing = st.number_input("Housing/Rent", min_value=0.0, value=1500.0)
        food = st.number_input("Food", min_value=0.0, value=600.0)
        transportation = st.number_input("Transportation", min_value=0.0, value=300.0)
        utilities = st.number_input("Utilities", min_value=0.0, value=200.0)
        education = st.number_input("Education", min_value=0.0, value=0.0)
        healthcare = st.number_input("Healthcare", min_value=0.0, value=150.0)
        entertainment = st.number_input("Entertainment", min_value=0.0, value=200.0)
        debt = st.number_input("Loan/Debt", min_value=0.0, value=0.0)
        other = st.number_input("Other", min_value=0.0, value=100.0)
        
    submitted = st.form_submit_button("Analyze Finances", type="primary", use_container_width=True)

if submitted:
    if not API_KEY:
        st.error("API Key is missing! Please add it to your .env file or Streamlit Secrets.")
        st.stop()
        
    expenses_dict = {
        "Housing": housing, "Food": food, "Transportation": transportation, 
        "Utilities": utilities, "Education": education, "Healthcare": healthcare, 
        "Entertainment": entertainment, "Debt": debt, "Other": other
    }
    
    # Process Deterministic Calculations
    metrics = calculate_financials(income, expenses_dict, savings)
    
    st.divider()
    st.markdown("<h2 style='color: #00F2FE !important;'>📊 Financial Overview (Calculated)</h2>", unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Expenses", f"{metrics['total_expenses']:,.2f}")
    m2.metric("Remaining Income", f"{metrics['remaining_income']:,.2f}")
    m3.metric("Savings Ratio", f"{metrics['savings_ratio']}%")
    m4.metric("Expense Ratio", f"{metrics['expense_ratio']}%")
    
    st.progress(metrics['preliminary_score'] / 100.0, text=f"Preliminary Health Score: {metrics['preliminary_score']}/100")
    
    inputs = {
        "monthly_income": income,
        "total_expenses": metrics['total_expenses'],
        "remaining_income": metrics['remaining_income'],
        "savings": savings,
        "savings_ratio": metrics['savings_ratio'],
        "expense_ratio": metrics['expense_ratio'],
        "financial_goal": goal,
        "expense_breakdown": str(expenses_dict)
    }

    st.markdown("<h3 style='color: white;'>🤖 AI Financial Analysis</h3>", unsafe_allow_html=True)
    with st.chat_message("assistant", avatar="✨"):
        st.write_stream(stream_recommendations(API_KEY, inputs))
        
    with st.spinner("Generating structured JSON insights..."):
        chain = get_financial_chain(API_KEY)
        raw_output = chain.invoke(inputs)
        result = parse_json_safely(raw_output.content)
        
        if result:
            r_level = result.get("risk_level", "UNKNOWN").upper()
            if "HIGH" in r_level: st.error(f"🚨 Risk Level: {r_level}")
            elif "MEDIUM" in r_level: st.warning(f"⚠️ Risk Level: {r_level}")
            else: st.success(f"🟢 Risk Level: {r_level}")
            
            t1, t2, t3 = st.tabs(["Spending & Priorities", "Budget Strategy", "Next Actions"])
            
            with t1:
                st.info(result.get("financial_summary", ""))
                st.markdown("**Spending Analysis**")
                for cat in result.get("spending_analysis", []):
                    st.write(f"- **{cat.get('category')}**: {cat.get('observation')} ➔ *{cat.get('recommendation')}*")
                st.markdown("**Top Priorities**")
                for p in result.get("top_priorities", []): st.write(f"✔️ {p}")
                
            with t2:
                st.markdown("**Budget Recommendations**")
                for b in result.get("budget_recommendations", []): st.write(f"- {b}")
                st.markdown("**Savings Strategy**")
                for s in result.get("savings_strategy", []): st.write(f"- {s}")
                
            with t3:
                st.markdown("**Next Month Action Plan**")
                for a in result.get("next_month_action_plan", []): st.write(f"🎯 {a}")
        else:
            st.error("Failed to parse the AI JSON output. Please try again.")
            st.code(raw_output.content)