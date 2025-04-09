#Finding the greatest of the 3 numbers by using functions
a = int(input("Enter a Number : "))
b = int(input("Enter a Number : "))
c = int(input("Enter a Number : "))

def great(a,b,c):
    if(a>b and a>c):
        return a 
    elif(b>c and b>a):
        return b
    elif(c>a and c>b):
        return c
 
print("The Greatest No. is : ",great(a,b,c))

#Converting Celcius into Farheniet by using functions
C = int(input("Enter the Celsius : "))
def temp(c):
    f = (C * 9/5) + 32
    return f
print("FARHENIET IS : ",temp(c)) 

#Calculating the Sum of first n natural numbers by using recurssion
n = int(input("Enter a Number : "))
def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n
print("The sum is : ",sum(n))

#Creating a star pattern using recursive
p = int(input("Enter a Number : "))
def pattern(p):
    if(p==0):
        return
    print("*" * p)
    pattern(p-1)
pattern(p)

