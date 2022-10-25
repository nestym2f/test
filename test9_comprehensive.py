nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."
"""
1. Find all of the numbers from 1–1000 that are divisible by 8
"""
def divBy8():
    newListDivBy8 = []
    for i in nums:
        if i % 8 == 0:
            newListDivBy8.append(i)
    return newListDivBy8

def divBy8Comp():
    newListDivBy8 = []
    newListDivBy8 = [i for i in nums if i % 8 == 0] 
                    
    return newListDivBy8
       
divBy8()
divBy8Comp()

    
    
