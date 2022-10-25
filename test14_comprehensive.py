nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."

"""
6. Use a dictionary comprehension to count the length of each word in a sentence
"""

def countWordDict():
    newStringList = string.replace('.', '')
    newStringList = newStringList.split(' ')
    newDict = {}
    for word in newStringList:
        newDict.update({word: len(word)})
    
    for key,value in newDict.items():
        print(f'Printing dictionary Word: {key} has {value} letters.')    
    return newDict

def countWordDictComp():
    newStringList = string.replace('.', '')
    newStringList = newStringList.split(' ')
    newDict = {word:len(word) for word in newStringList}
    for key,value in newDict.items():
        print(f'Printing dictionary Word: {key} has {value} letters.')    
    return newDict
    
    
countWordDict()
countWordDictComp()
