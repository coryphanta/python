# Result of the sportsmen in the first day
print("Please enter the result of the sportsmen in the first day")
firstDayResult = input()

# Target result
print("Please enter the target result")
targetResult = input()

# Calculate the number of day when  the target result will be achieved
# If every day the result is increasing to 10%
numberTrainingDays = 1
intermediateResult = int(firstDayResult)
while intermediateResult < int(targetResult):
    numberTrainingDays = numberTrainingDays + 1
    intermediateResult = intermediateResult + (intermediateResult * 0.1)
print("Number of the target result day: " + str(int(numberTrainingDays)))
