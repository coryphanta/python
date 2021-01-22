# Ask user for the revenue and expenses.
print("Please enter the amount of revenue")
revenue = input()
print("Please enter the amount of expenses")
expenses = input()

# Calculate the financial result of the company
financialResults = int(revenue) - int(expenses)

# Print the message about financial result
if financialResults < 0:
    print("What is the currency")
    currency = input()
    print("Oh noooo! Your result is negative: " + str(financialResults) + " " + currency)
elif financialResults == 0:
    print("Push a little! You are at a break even point")
else:
    # Calculate the profit margin
    print("What is the currency")
    currency = input()
    profit = (financialResults / int(revenue)) * 100
    print("Profitable is " + str(int(profit)) + "%")

    # Ask user the number of employees of the company
    print("How much employees?")
    employees = input()

    # Calculate profit per employee
    employeeProfit = financialResults / int(employees)
    print("Profit per employee: ~" + str(int(employeeProfit)) + " " + currency)
