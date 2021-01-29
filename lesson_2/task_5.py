# Implement the "Rating" structure, which is a non-increasing set of natural numbers.
ratingList = [7, 5, 3, 3, 2]

# The user needs to request a new rating item.
print("Enter any number")
inputNumber = int(input())

currentIndex = 0
indexToAdd = 0

# If there are elements in the rating with the same values,
# then a new element with the same value should be placed after them.
for i in ratingList:
    # Calculating an index within a sequence
    if inputNumber == i:
        indexToAdd = currentIndex
    elif inputNumber > i:
        if currentIndex > 0:
            indexToAdd = currentIndex
            break
        else:
            # If need to add to the start of sequence
            indexToAdd = 0
            break
    else:
        # If need to add to the end of sequence
        indexToAdd = currentIndex + 1
    currentIndex = currentIndex + 1

ratingList.insert(indexToAdd, inputNumber)
print(ratingList)
