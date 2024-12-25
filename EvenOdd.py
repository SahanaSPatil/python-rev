"""
Given a positive integer x. Your task is to check, if it is even or odd
(Any number that gives zero as remainder when divided by 2 is an even number)

"""

def checkOddEven(x):
    if(x % 2):
        print("Odd")
    else:
        print("Even")
        

X = int(input("Enter a number : "))
checkOddEven(X)
    

