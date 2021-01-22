# Ask user to enter any number
print("Please enter any number")
userInputNumber = input()

# Find a sum of numbers n+nn+nnn

sumOfNumbers = int(userInputNumber) + (int(userInputNumber) * int(userInputNumber)) + (
            int(userInputNumber) * int(userInputNumber) * int(userInputNumber))

print("Result: " + str(sumOfNumbers))
