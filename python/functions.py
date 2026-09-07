# Basic Function
def greet():
    print("Hello!")
greet()


# Function with Parameter
def greet_user(name):
    print("Hello,", name)
greet_user("Abeera")


# Multiple Parameters
def add(a, b):
    print(a + b)
add(10, 20)


# Return Value
def multiply(a, b):
    return a * b
result = multiply(5, 4)
print(result)


# Default Parameter
def welcome(name="Guest"):
    print("Welcome,", name)
welcome("coders")


# Keyword Arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)
student(age=19, name="Abeera")


# Multiple Return Values
def calculate(a, b):
    return a + b, a - b
addition, subtraction = calculate(10, 5)
print(addition)
print(subtraction)


# *args
def numbers(*args):
    print(args)
numbers(10, 20, 30, 40)


# Function with Loop
def print_numbers(numbers):
    for number in numbers:
        print(number)
print_numbers([1, 2, 3, 4, 5])


# Function with Condition
def check_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even(10))
print(check_even(7))

# Function Calling Another Function
def square(number):
    return number * number


def display_square(number):
    result = square(number)
    print("Square:", result)
display_square(6)