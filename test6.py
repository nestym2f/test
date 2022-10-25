def orderList(unsortedList):
    change = True
    
    while change:
        change = False
        for i in range(len(unsortedList) - 1):
            if unsortedList[i] > unsortedList[i+1]:
                temp = unsortedList[i+1]
                unsortedList[i+1] = unsortedList[i]
                unsortedList[i] = temp
                change = True
                
            
    
    print(unsortedList)
    
    
orderList([1,2,4,52,22,12,54,4])