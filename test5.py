

def multipleActions(stringToAction):
    unsortedList = []
    sumDigits = 0
    for i in stringToAction:
        try:
            x = int(i)
            unsortedList.append(x)
            sumDigits = sumDigits + x
        except:
            continue
    unsortedList.sort()
    sortedList = unsortedList.copy()
    stringChain = "".join(map(str, sortedList))      
        
    print(stringChain)
    print(sumDigits)
    
    
    
    
    
    
    
    
multipleActions('j1yWqALylXuvZkFBkZ5i7D8Db6MwnwwE')