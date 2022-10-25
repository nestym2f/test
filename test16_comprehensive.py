nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."
"""
8. For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest
single digit any of the numbers is divisible by
"""

def highestDiv():
    newDict = {}
    for i in nums:
        for j in range(1,10):
            if i % j == 0:
                newDict[i] = j
    return newDict
            
def highestDivComp():
    newDict = {i:j for i in nums for j in range(1,10) if i % j == 0}
    q8_answer = {num:max([divisor for divisor in range(1,10) if num % divisor == 0]) for num in nums} 
    return newDict
               
highestDiv()
highestDivComp()