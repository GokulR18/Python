#Finding the greatest No. among the all the 4 numbers
a = int(input("Enter No. 1 :"))
b = int(input("Enter No. 2 :"))
c = int(input("Enter No. 3 :"))
d = int(input("Enter No. 4 :"))

if (a>b and a>c and a>d):
    print("The Greatest no. is : ",a)
    
elif (b>c and b>d and b>a):
    print("The Greatest no. is : ",b)

elif (c>d and c>a and c>b):
    print("The Greatest no. is : ",c)

elif (d>a and d>b and d>c):
    print("The Greatest no. is : ",d)

#Taking Marks from user and Grading them according to their Percentage
M1 = int(input("Enter your Marks :"))
M2 = int(input("Enter your Marks :"))
M3 = int(input("Enter your Marks :"))

P = ((M1+M2+M3)*100)/300

if (P >= 90 <= 100):
    print("You got A grade, your percentage is :", P)
elif(P >= 70 < 90):
    print("You got B grade, your percentage is :", P)
elif(P >= 50 < 70):
    print("You got C grade, your percentage is :", P)
elif(P >= 40 < 50):
    print("You got D grade, your percentage is :", P)
else:
    print("You are fail :( , Your percentage is :",P)

if(M1 <= 39):
    print("YOU have to focus on M1")
if(M2 <= 39):
    print("YOU have to focus on M2")
if(M3 <= 39):
    print("YOU have to focus on M3")

#Checking whether the users name is in the List or not
List = ["Gokul","Shweta","Akansha","Yogesh","Arpith","Gyan"]
Name = input("Enter your name : ")

if (Name in List):
    print("Your name is in the LIst")
else :
    print("Sorry, Your name is not it the List")





    








