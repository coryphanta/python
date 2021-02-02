# The user enters the month as an integer from 1 to 12
dictionary = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer', 7: 'Summer', 8: 'Summer', 9: 'Autumn', 10: 'Autumn', 11: 'Autumn', 12: 'Winter'}

listOfSeasons = ['Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer', 'Autumn', 'Autumn', 'Autumn', 'Winter']

print("Please enter the month")
month = input()

# Calculate the season
season = dictionary.get(int(month))
if int(month) not in dictionary:
    raise Exception("Nononono! Only from 1 to 12")

print("Season is: " + str(season) + ". Found in the dictionary")

season = listOfSeasons[int(month) - 1]
print("Season is: " + str(season) + ". Found in the list")
