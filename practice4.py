#CREATING A SMALL DICTIONARY BY USING DICTIONARY
DICT = {"AAGNI" : "FIRE",
        "PAANI" : "WATER",
        "VAAYU" : "AIR",
        "BHOOMI" : "LAND"
}
Word = input("Enter the word whose meaning you want to know :  ")
print(DICT[Word])

#TAKING NUMBERS AS INPUT AND DIPLAYING ONLU THE UNIQUE NUMBERS
Set = set()
n1= int(input("Enter number :"))
Set.add(n1)
n2= int(input("Enter number :"))
Set.add(n2)
n3= int(input("Enter number :"))
Set.add(n3)
n4= int(input("Enter number :"))
Set.add(n4)
n5= int(input("Enter number :"))
Set.add(n5)
n6= int(input("Enter number :"))
Set.add(n6)
n7= int(input("Enter number :"))
Set.add(n7)
n8= int(input("Enter number :"))
Set.add(n8)
print(Set) 

#ADDING DATA OF STUDENTS AND THERE MARKS INTO AN EMPTY DICTIONARY
x = {}
NAME = input("Enter the Name :")
MARKS = input("Enter the Marks")
x.update({NAME : MARKS})

NAME = input("Enter the Name :")
MARKS = input("Enter the Marks")
x.update({NAME : MARKS})

NAME = input("Enter the Name :")
MARKS = input("Enter the Marks")
x.update({NAME : MARKS})

NAME = input("Enter the Name :")
MARKS = input("Enter the Marks")
x.update({NAME : MARKS})

print(x)