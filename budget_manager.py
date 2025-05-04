from expense_manager import expenses

budget = None

def track_budget():
    global budget

    if budget is None:
        try:
            budget_input = input("No budget set. Enter your monthly budget amount: ").strip()
            budget = float(budget_input)
            if budget <= 0:
                print("❌ Budget must be a positive number.\n")
                budget = None
                return
            print(f"✅ Monthly budget set to Rs. {budget:.2f}\n")
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.\n")
            return

    total_expense = sum(exp['amount'] for exp in expenses)
    print(f"Total expenses so far: Rs. {total_expense:.2f}")

    if total_expense > budget:
        print("⚠️ Warning: You have exceeded your budget!\n")
    else:
        print(f"You have Rs. {budget - total_expense:.2f} remaining for the month.\n")
