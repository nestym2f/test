def largestRange(array):
    array.sort()
    orderedArray = array.copy()
    orderedArraySize = len(orderedArray)
    outputArray = [0,0]
    maxSize = 0
    tempMaxSize = 0
    for i in range(orderedArraySize):
        if tempMaxSize > maxSize or maxSize == 0:
            outputArray[0] = orderedArray[i]
        if orderedArray[i]+1 == orderedArray[i+1]:
            tempMaxSize += 1
            if tempMaxSize >= maxSize:
                maxSize += 1
                outputArray[1] = orderedArray[i+1]
        else:
            tempMaxSize = 0
            
    """for i in range(len(orderedArray)):
        for j in range(i + 1,len(orderedArray)):
            if tempMaxSize >= maxSize:
                outputArray[0] = orderedArray[i]
            if orderedArray[j+1] - 1 == orderedArray[j]:
                maxSize += 1
                tempMaxSize += 1
                outputArray[1] = orderedArray[j+1]
            else:
                tempMaxSize = 0
                break"""
        
    print(orderedArray)
    
    
    
largestRange([1,11,3,0,15,5,2,4,10,7,12,6])