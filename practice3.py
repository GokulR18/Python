#TAKING INPUT FROM THE USER AND ADDING IT INTO THE LIST
fruits = [] 
F1 = input("Enter a Fruit Name : ")
fruits.append(F1)
F2 = input("Enter a Fruit Name : ")
fruits.append(F2)
F3 = input("Enter a Fruit Name : ")
fruits.append(F3)
F4 = input("Enter a Fruit Name : ")
fruits.append(F4)
F5 = input("Enter a Fruit Name : ")
fruits.append(F5)
F6 = input("Enter a Fruit Name : ")
fruits.append(F6)
F7 = input("Enter a Fruit Name : ")
fruits.append(F7)
print(fruits) 

#TAKING DATA FROM USER AND SAVING IT INA LIST IN A SORTED MANNER
Marks = [] 
F1 = int(input("Enter your Marks: "))
Marks.append(F1)
F2 = int(input("Enter your Marks: "))
Marks.append(F2)
F3 = int(input("Enter your Marks: "))
Marks.append(F3)
F4 = int(input("Enter your Marks: "))
Marks.append(F4)
F5 = int(input("Enter your Marks: "))
Marks.append(F5)
F6 = int(input("Enter your Marks: "))
Marks.append(F6)
F7 = int(input("Enter your Marks: "))
Marks.append(F7)
Marks.sort()
print(Marks)

#SUM OF THE MARKS
print(sum(Marks))

#COUNTING THE NUMBER OF ELEMENTS IN A TUPLE
A = (1,0,4,5,0,1,0,4,2,5,0)
B = A.count(0)
print(B)
