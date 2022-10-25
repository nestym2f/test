"""
Given a list of numbers, remove floats (numbers with decimals)

Find all of the numbers from 1-1000 that are divisible by 7

Find all of the numbers from 1-1000 that have a 3 in them

Count the number of spaces in a string

Create a list of all the consonants in the string “Yellow Yaks like yelling and 
yawning and yesturday they yodled while eating yuky yams”

Get the index and the value as a tuple for items in the list 'hi', 4, 8.99, 'apple','t','b','n'. 
Result would look like (index, value), (index, value)

Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, 
list_b = 2, 3, 4, 5

Get only the numbers in a sentence like 'In 1984 there were 13 instances of a protest 
with over 1000 people attending'

Given numbers = range(20), produce a list containing the word 'even' if a number in the numbers is even,
and the word 'odd' if the number is odd. Result would look like 'odd','odd', 'even'

Produce a list of tuples consisting of only the matching numbers in these lists list_a = 1, 2, 3,4,5,6,7,8,9,
list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)

Find all of the words in a string that are less than 4 letters

Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
"""
from unicodedata import digit, numeric


original_list = [2,3.75,.04,59.354,6,7.7777,8,9,14]
nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."
string2 = 'Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'
tupleList = ['hi', 4, 8.99, 'apple','t','b','n']
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
sentence = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
list_c = [1, 2, 3,4,5,6,7,8,9]
list_d = [2, 7, 1, 12]

def removeDecimals():
    newList = [integerNumber for integerNumber in original_list if isinstance(integerNumber,int)]
    print(newList)
removeDecimals()

def divBy7():
    newList = [divNumber for divNumber in original_list if divNumber % 7 == 0]
    print(newList)
divBy7()

def numbersWith3():
    newList = [numberWith3 for numberWith3 in nums if '3' in str(numberWith3)]
    print(newList)
numbersWith3()

def countSpaces():
    counterSpaces = len([char for char in string if char == ' '])
    print(counterSpaces)
countSpaces()

def consonentList():
    newList = [char for char in string2 if char not in ['a', 'e', 'i', 'o', 'u',' ','.']]
    print(newList)
consonentList()

def consonentListNoRepeat():
    newList = [char for char in string2 if char not in ['a', 'e', 'i', 'o', 'u',' ','.']]
    newListNRepeat = []
    for charN in newList:
        if charN not in newListNRepeat:
            newListNRepeat.append(charN)
    print(newListNRepeat)
consonentListNoRepeat()

def valueAsTuple():
    newDict = {listIndex:listvalue for listIndex, listvalue in enumerate(tupleList)}
    print(newDict)
valueAsTuple()
    
def commonNumbers():
    newList = [a for a in list_a if a in list_b]
    print(newList)
commonNumbers()

def getOnlyNumbers():
    sentenceToList = sentence.split(' ')
    numbersOnlyList = [x for x in sentenceToList if not x.isalpha()]
    
    print(numbersOnlyList) 
getOnlyNumbers()

def evenOddNumbers():
    listNumbers = ['even' if a % 2 == 0 else 'odd' for a in range(20)]
    print(listNumbers)
evenOddNumbers()

def checkMatchingNumbers():
    newDict = {x:y for x in list_c for y in list_d if x == y}
    print(newDict)
checkMatchingNumbers()

def lessThan4():
    newList = sentence.split(' ')
    listToPrint = [x for x in newList if len(x) < 4]
    print(listToPrint)
lessThan4()

def divBy2_9():
    newList = [x for x in range(1,1001) if([True for y in range(2,10) if x % y == 0])]
    print(newList)
divBy2_9()

def pythonIsAwesome():
    word = 'Python is awesome'
    n = len(word)
    word1 = word.upper()
    word2 = word.lower()
    converted_word = ''
    for i in range(n):
        if i%2==0:
            converted_word +=word2[i]
        else:
            converted_word +=word1[i]
    print(converted_word)
pythonIsAwesome()