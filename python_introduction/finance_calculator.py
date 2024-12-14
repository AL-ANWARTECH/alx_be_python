# User Monthly Income
monthly_income = float(input("Enter Your Monthly Income: "))
# User  Total Monthly Expenses
monthly_expenses = float(input("Enter Your Total Monthly Expenses: "))
# Calculate Monthly savings
monthly_savings = monthly_income - monthly_expenses
# Calculate projected annual savings with a 5% interest rate
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)
# Output result
print(f"Your monthly savings are ${monthly_savings: .2f}.")
print(f"Projected savings after one year, with interest, is:${projected_savings: .2f}.")
