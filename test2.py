def printFizzBuzz(x,y):
    begin = x
    end = y
    while begin <= end:
        if begin % 5 == 0 and begin % 3 == 0:
            print("FizzBuzz")
        elif begin % 3 == 0:
            print("Buzz")
        elif begin % 5 == 0:
            print("Fizz")
        else:
            print(begin)
        begin += 1
            
printFizzBuzz(1,15)