# For a list, implement the exchange of values of adjacent elements
listOfElements = []

print("Please enter the number of elements of the list: ")
listSize = input()

if int(listSize) < 2:
    raise Exception("Are you kidding? No magic if the number of elements is less than two")

# Filling the list with custom values
for i in range(0, int(listSize)):
    print("Please enter the '" + str(i) + "' element:")
    element = input()
    listOfElements.append(element)

print("List is: ")
print(listOfElements)

print("Now magic will happen and adjacent elements will be swapped!")

# Swap adjacent elements
# If the number of elements is odd, save the last one in its place.
index = 0
for i in listOfElements:
    i = int(i)
    index = index + 1
    print("not(index == int(listSize)) " + str(index) + "==" + str(int(listSize)))
    print("(index % 2) > 0 " + str((index % 2) > 0))
    if not (index == int(listSize)) and (index % 2) > 0:
        print("index " + str(index))
        listOfElements[index - 1], listOfElements[index] = listOfElements[index], listOfElements[index - 1]

print("List after the magic: " + str(listOfElements))
