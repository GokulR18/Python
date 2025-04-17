import math

# 1. Programmer Class
class Programmer:
    def __init__(self, name, language, company="Microsoft"):
        self.name = name
        self.language = language
        self.company = company

    def show(self):
        print(f"Name: {self.name}, Language: {self.language}, Company: {self.company}")


# 2. Calculator Class
class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def square_root(self):
        return math.sqrt(self.number)

    # 4. Static method
    @staticmethod
    def greet():
        print("Hello! Welcome to the Calculator.")


# 3. Class attribute test
class Demo:
    a = 5  # Class attribute

# 5. Train class
class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def get_status(self):
        print(f"Train Name: {self.name}")
        print(f"Available Seats: {self.seats}")

    def fare_info(self):
        print(f"Fare for this train is ₹{self.fare}")

    def book_ticket(self):
        if self.seats > 0:
            self.seats -= 1
            print("Ticket booked successfully!")
        else:
            print("Sorry, no seats available.")


# 6. Changing self to another name
class Example:
    def __init__(harry, value):  # self replaced with 'harry'
        harry.value = value

    def display(harry):
        print(f"The value is {harry.value}")


# --- Testing all classes ---

# Task 1
print("Programmer Example")
p1 = Programmer("Alice", "Python")
p1.show()

# Task 2 & 4
print("Calculator Example")
calc = Calculator(16)
Calculator.greet()
print("Square:", calc.square())
print("Cube:", calc.cube())
print("Square Root:", calc.square_root())

# Task 3
print("Class Attribute Change Test")
d = Demo()
print("Original class attribute a:", Demo.a)
d.a = 0
print("Changed object attribute a:", d.a)
print("Class attribute a after change:", Demo.a)

# Task 5
print("Train Example")
t = Train("Rajdhani Express", 1500, 2)
t.get_status()
t.fare_info()
t.book_ticket()
t.book_ticket()
t.book_ticket()
t.get_status()

# Task 6
print("Changing self Parameter")
e = Example(42)
e.display()
