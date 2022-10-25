nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."

"""
7. Use a nested list comprehension to find all of the numbers from 1–1000 
that are divisible by any single digit besides 1 (2–9)
"""

def checkDivNumber():
    newListDiv = []
    for i in nums:
        for j in range(2,10):
            if i % j == 0:
                newListDiv.append(i)
                break
    return newListDiv

def checkDivNumberComp():
    newListDiv = [i for i in nums for j in range(2,10) if i % j == 0 ]
    newListDiv = [i for i in nums if True in [True for dig in range(2,10) if i % dig == 0]]
   
    q7_answer = [num for num in nums if True in [True for divisor in range(2,10) if num % divisor == 0]]
    return newListDiv

checkDivNumber()
checkDivNumberComp()