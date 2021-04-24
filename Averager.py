import statistics

average = input("What average type do you want: mean, median, mode: ")
numbers = input("Please input numbers: ")

meanAverageNumbers = [int(i) for i in numbers.split() if i.isdigit()]
modeAverageNumbers = [int(i) for i in numbers.split() if i.isdigit()]
medianAverageNumbers = [int(i) for i in numbers.split() if i.isdigit()]

meanAverage = statistics.mean(meanAverageNumbers)
modeAverage = statistics.mode(modeAverageNumbers)
medianAverage = statistics.median(medianAverageNumbers)

if average == "mode":
    print(modeAverage)

if average == "mean":
    print(meanAverage)

if average == "median":
    print(medianAverage)
