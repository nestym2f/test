"""
1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
also create a lambda function that multiplies argument x with argument y and print the result. Go to the editor
Sample Output:
25
48

2. Write a Python program to create a function that takes one argument, 
and that argument will be multiplied with an unknown given number. Go to the editor
Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75

3. Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

4. Write a Python program to sort a list of dictionaries using Lambda. Go to the editor
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
"""
def function1(a):
    y = lambda x: x + 15
    print(y(a))
function1(10)

def function1_2(a,b):
    lambFunction = lambda x,y: x * y
    print(lambFunction(a,b))
function1_2(8,6)

def function_2(x):
    lambfunction = lambda y: x * y
    print(lambfunction(15))
function_2(3)

def function_3():
    tupleList = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
    tupleList.sort(key = lambda x: x[1])
    print(tupleList)
function_3()

def function_4():
    tupleDict = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
    AllSorted = sorted(tupleDict, key = lambda x: x['color'],reverse=True)
    print(AllSorted)
function_4()
"""
5. Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
def function_5():
    listNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evenNumbers = list(filter(lambda x: x % 2 == 0,listNumbers))
    print(evenNumbers)
    oddNumbers = list(filter(lambda x: x % 2 != 0,listNumbers))
    print(oddNumbers)
    evenNumbers = [x for x in listNumbers if x % 2 == 0]
    print(evenNumbers)
    oddNumbers = [x for x in listNumbers if x % 2 != 0]
    print(oddNumbers)
function_5()
    