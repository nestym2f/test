nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."
"""
2. Find all of the numbers from 1–1000 that have a 6 in them
"""
def hasA6():
    hasA6List = []
    for i in nums:
        if '6' in str(i):
            hasA6List.append(i)
    return hasA6List
            
def hasA6Comp():
    hasA6List = []
    hasA6List = [i for i in nums if '6' in str(i)]
    return hasA6List

hasA6()
hasA6Comp()