import random
n = random.randint(1,100)
a = -1
guess = 1
while(a != n):
    a = int(input("Guess the Number : "))
    if (a>n):
        print("Lower Number please")
        guess += 1
    elif(a<n):
        print("Higher Number please")
        guess += 1

print(f"You have guessed the Number {n} in {guess} attempts")
    



