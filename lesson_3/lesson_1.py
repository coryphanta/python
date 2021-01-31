# Implement a function that takes two numbers (positional arguments) and performing their division.
def divide_numbers(x, y):
    # handling the situation of division by zero
    if y == 0:
        raise Exception("Nononono! Don't you know that you can't divide by zero?")
    return x / y


# Request from user for numbers
inputDividend = int(input("Please enter a dividend"))
inputDivider = int(input("Please enter a divider"))

print("The result of divide is: " + str(divide_numbers(inputDividend, inputDivider)))
