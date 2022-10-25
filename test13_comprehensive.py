from typing import Counter


nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."

"""
5. Find all of the words in a string that are less than 5 letters
"""

def findWordsLessThan5():
    wordCounter = 0
    newString = string.replace('.','')
    newString = newString.split(' ')
    for word in newString:
        if len(word) < 5:
            wordCounter += 1
    print(wordCounter)       
    return wordCounter

def findWordsLessThan5Comp():
    newString = string.replace('.','')
    newString = newString.split(' ')
    wordCounter = len([char for char in newString if len(char) < 5])
    print(wordCounter)       
    return wordCounter


findWordsLessThan5()