#Creating a Table
n = int(input("Enter a Number : "))
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")


#Finding wether a number is prime or not
v = int(input("Enter a Number : "))
for i in range(2,v):
    if(v%i) == 0:
        print("The Number is not a Prime Number")
        break
else:
    print("The Number is a Prime Number")
        

#Print the names of people whose names start with S
list = ["Shweta","Gokul","Swati","Shubham","Gyan","Akansha","Yogesh"]
for i in list:
    if(i.startswith("S")):
        print(i)
    
#Finding the Factorial of a number
f = int(input("Enter a Number: "))
P = 1
for i in range(1,f+1):
    P= P*i
print(f"The Factorial of {f} is {P}")

#Creating a star Pattern
s =int(input("Enter a Number : "))
for i in range(1,s+1): #for pyramid Pattern
    print(" "* (s-i), end="")
    print("*"* (2*i-1), end="")
    print("")
    
for i in range(1,s+1): #for Ladder Pattern
    print("*"* (2*i-1), end="")
    print("")

