nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."
"""
4. Remove all of the vowels in a string
"""
def removeVowels():
    newString = string
    for i in string:
        if i in ['a','e','i','o','u']:
            newString = newString.replace(i,'')
    print(newString)
    return newString
            
def removeVowelsComp():
    newString = [i for i in string if i not in ['a','e','i','o','u']]
    newString = ''.join(newString)
    print(newString)
    return newString
            
            
removeVowels()
removeVowelsComp()