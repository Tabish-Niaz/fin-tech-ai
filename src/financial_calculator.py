def calculate_financials(income, expenses, savings):
    total_expenses = sum(expenses.values())
    remaining_income = income - total_expenses
    
    # Divide by zero error se bachne ke liye checks
    savings_ratio = (savings / income) * 100 if income > 0 else 0
    expense_ratio = (total_expenses / income) * 100 if income > 0 else 0

    # Rule-based Preliminary Score (0-100)
    score = 50 
    if savings_ratio >= 20: score += 20
    elif savings_ratio >= 10: score += 10
    if expense_ratio <= 50: score += 20
    elif expense_ratio <= 80: score += 10
    else: score -= 20
    if remaining_income < 0: score -= 30

    score = max(0, min(100, score))

    return {
        "total_expenses": total_expenses,
        "remaining_income": remaining_income,
        "savings_ratio": round(savings_ratio, 2),
        "expense_ratio": round(expense_ratio, 2),
        "preliminary_score": round(score, 2)
    }