# The user enters a string of several words separated by spaces
print("Please enter any sentence")
sentence = input()

listOfWords = sentence.split(" ")

# Print each word on a new line
# The lines must be numbered
index = 1
# If the word is long, print only the first 10 letters in the word.
for i in listOfWords:
    if len(i) > 10:
        print(str(index) + ". " + i[:10])
    else:
        print(str(index) + ". " + i)
        index = index + 1
