"""
Given a positive integer x. Your task is to check, if it is even or odd
(Any number that gives zero as remainder when divided by 2 is an even number)

"""

def checkOddEven(x):
    if(x % 2):
        print("Odd")
    else:
        print("Even")
        
"""
Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

Return True for the following cases:

Either a or b (not both) is non-negative and the flag is false.
Both a and b are negative and the flag is true.
Otherwise, return False.
"""

def checkStatus(a, b, flag):
    if(a >= 0 and b < 0 and flag == False):
        return True
    
    elif(a < 0 and b >= 0 and flag == False):
        return True
    
    elif(a < 0 and b < 0 and flag):
        return True
    
    else:
        return False
    
        

#X = int(input("Enter a number : "))
#checkOddEven(X)
    
a = int(input("Enter a number(a) : "))
b = int(input("Enter a number(b) : "))
flag = int((input("Enter 0/1 : ")))
print(checkStatus(a , b , flag))
