def checkSum(numbers, n):
    returnNow = False
    listSum =[]
    for i in numbers:
        if returnNow:
            break
        for j in numbers:
            if j + i == n:
                returnNow = True
                listSum = [i,j]
                break
    print(listSum)




checkSum([14,13,6,9,0,12,4,16,1,2],30)
