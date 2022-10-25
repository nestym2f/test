def calAvg(newSet):
    finalResult = 0
    for i in newSet:
        finalResult += i
    averageResult = finalResult / len(newSet)   
    print(averageResult)

calAvg({1,26,34,4,51,66,7,8,9,25,42})

        