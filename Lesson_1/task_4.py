#User enter positive whole number
print("Please enter any positive whole number")
anyNumber = input()
anyNumberIterator = iter(anyNumber)
buffer = 0

#Find the biggest number in the user number
try:
    while num := next(anyNumberIterator):
        if int(num) > buffer:
            buffer = int(num)
except StopIteration:
    print("The biggest number is: " + str(buffer))
