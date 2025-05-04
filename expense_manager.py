import csv
import os

expenses = []

from datetime import datetime

VALID_CATEGORIES = ["Food", "Travel", "Transport", "Entertainment", "Bills", "Health", "Shopping", "Utilities", "Other"]

def add_expense():
    try:
        date_str = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("❌ Invalid date format. Use YYYY-MM-DD.\n")
            return

        print("Available categories:", ", ".join(VALID_CATEGORIES))
        category_input = input("Enter category from above list: ").strip()
        if not category_input or category_input.title() not in VALID_CATEGORIES:
            print("❌ Invalid category. Please choose from the list.\n")
            return
        category = category_input.title()

        amount_str = input("Enter amount: ").strip()
        try:
            amount = float(amount_str)
            if amount <= 0:
                print("❌ Amount must be a positive number.\n")
                return
        except ValueError:
            print("❌ Invalid amount. Enter a numeric value.\n")
            return

        description = input("Enter description: ").strip()
        if not description:
            print("❌ Description cannot be empty.\n")
            return

        expense = {
            'date': date_str,
            'category': category,
            'amount': amount,
            'description': description
        }
        expenses.append(expense)
        print("✅ Expense added successfully!\n")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}\n")

def view_expenses():
    if not expenses:
        print("No expenses to show.\n")
        return
    print("\nExpenses:")
    for idx, exp in enumerate(expenses, 1):
        if all(k in exp for k in ['date', 'category', 'amount', 'description']):
            print(f"{idx}. {exp['date']} | {exp['category']} | Rs. {exp['amount']} | {exp['description']}")
        else:
            print(f"{idx}. Incomplete entry skipped.")
    print()

def save_expenses(filename="expenses.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
        writer.writeheader()
        for exp in expenses:
            writer.writerow(exp)
    print("Expenses saved to file.\n")

def load_expenses(filename="expenses.csv"):
    if not os.path.exists(filename):
        return
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                row['amount'] = float(row['amount'])
                expenses.append(row)
            except ValueError:
                continue
