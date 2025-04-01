NAME = input("Enter your Name :")
print("Good Morning ",NAME)
DATE = input(" ENter a Date :")

Letter = '''DEAR NAME,
YOUR ARE SELECTED
DATE'''
print(Letter.replace("NAME", NAME).replace("DATE",DATE))
print(NAME.find("A")) 
 