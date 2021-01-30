# Implement a function my_func () that takes three positional arguments
def my_func(x, y, z):
    min_element = x
    arg1 = 0
    arg2 = 0
    sequence = [x, y, z]
    for i in sequence:
        if i < min_element:
            min_element = i
    for i in sequence:
        if i != min_element and arg1 == 0:
            arg1 = i
        elif i != min_element and int(arg1) > 0:
            arg2 = i
# And returns the sum of the largest two arguments.
    return int(arg1) + int(arg2)


inputX = input("Please enter the first number ")
inputY = input("Please enter the second number ")
inputZ = input("Please enter the third number ")

print("Sum of the biggest numbers is: " + str(my_func(inputX, inputY, inputZ)))
