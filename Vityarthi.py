print("Welcome to My Daily Expense Tracker!")
print("Let's keep track of your daily spending and budget.\n")

daily_budget = float(input("Enter your daily budget amount: "))

expenses = []

while True:
    category = input("Enter expense category (or type 'done' to finish): ")
    if category.lower() == 'done':
        break

    amount = float(input(f"Enter amount spent on {category}: "))
    
    expenses.append((category, amount))
    
    total_spent = sum(amount for _, amount in expenses)
    
    print(f"Total spent so far: {total_spent:.2f}")
    
    if total_spent > daily_budget:
        print("Oops! You've exceeded your daily budget.\n")
    else:
        print("You're within your budget. Keep it up!\n")

print("\n--- Expense Summary ---")
for cat, amt in expenses:
    print(f"{cat}: {amt:.2f}")

total_spent = sum(amount for _, amount in expenses)
savings = daily_budget - total_spent
print(f"\nTotal spent: {total_spent:.2f}")
print(f"Remaining savings: {savings:.2f} (if positive)")

print("\nThanks for using this tracker! Manage your money smartly.")