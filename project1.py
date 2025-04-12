#Stone paper Sizzor Game using Python
import random
computer = random.choice([1,2,3])
youstr = input("Enter your choice : ")
dict = {"Stone" : 1 ,"Paper" : 2 , "Sizzor" : 3}
reversedict = {1 : "Stone", 2 : "Paper", 3 :"Sizzor"}
you = dict[youstr]


print(f"YOu chose {reversedict[you]} And Computer chose {reversedict[computer]}")
if(computer==you):
    print("Its a Draw")
else:
    if(computer == 1 and you == 2):
        print("YOU WIN")
    elif(computer == 1 and you == 3):
        print("YOU LOSE")
    elif(computer == 2 and you == 1):
        print("YOU LOSE")
    elif(computer == 2 and you == 3):
        print("YOU WIN")
    elif(computer == 3 and you == 1):
        print("YOU WIN")
    elif(computer == 3 and you == 2):
        print("YOU LOSE")