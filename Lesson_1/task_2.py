# User is typing time in seconds

print("Please type time in seconds")
timeInSecondsInput = input()

# Convert the time into hours, minutes and seconds and output in the format hh: mm: ss
timeInSecondsInt = int(timeInSecondsInput)
hours = timeInSecondsInt // 3600

if hours == 0:
    minutes = timeInSecondsInt // 60
else:
    minutes = hours // 60
if minutes == 0:
    seconds = timeInSecondsInt
else:
    seconds = timeInSecondsInt % 60

    printableHours = hours
    printableMinutes = minutes
    printableSeconds = seconds
if hours < 10:
    printableHours = str("0"+str(hours))
if minutes < 10:
    printableMinutes = str("0"+str(minutes))
if seconds < 10:
    printableSeconds = str("0"+str(seconds))
print("%s:%s:%s" % (printableHours, printableMinutes, printableSeconds))
