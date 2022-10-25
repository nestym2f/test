nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."
"""
3. Count the number of spaces in a string
"""
def countSpaces():
    countSpaces = 0
    for i in string:
        if i == ' ':
            countSpaces += 1
    return countSpaces

def countSpacesComp():
    countSpaces = 0
    countSpaces = len([i for i in string if i == ' '])
    
    return countSpaces

countSpaces()
countSpacesComp()

    
