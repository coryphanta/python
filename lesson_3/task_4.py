# The program accepts a real positive x and a negative integer y.
# It is necessary to raise the number x to the power of y.
def my_func(x, y):
    if x < 0:
        raise Exception("Nononono! The first number should be positive")
    if y >= 0:
        raise Exception("Nononono! The second number should be negative")

    # The first way. Exponentiation using the ** operator.
    print("the first way result " + str(x ** y))

    # The second way. Using loop
    index = abs(y)
    exponentiation_result = x
    while index > 1:
        exponentiation_result = exponentiation_result * x
        index = index - 1

    print("the first way result " + str(1 / exponentiation_result))


inputX = int(input("Please enter the first number "))
inputY = int(input("Please enter the second number "))

print(my_func(inputX, inputY))
