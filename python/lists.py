

# Creating a List
fruits = ["apple", "banana", "mango", "orange"]
print(fruits)


# Accessing List Items
print(fruits[0])
print(fruits[-1])


# Changing List Items
fruits[1] = "grapes"
print(fruits)


# Adding Items
fruits.append("watermelon")
fruits.insert(1, "kiwi")
print(fruits)


# Removing Items
fruits.remove("apple")
fruits.pop()
print(fruits)


# List Slicing
print(fruits[1:3])
print(fruits[:2])
print(fruits[2:])


# Looping Through a List
for fruit in fruits:
    print(fruit)


# List Methods
numbers = [5, 2, 8, 1, 3]

numbers.append(10)
numbers.insert(0, 7)
numbers.remove(8)
numbers.sort()
numbers.reverse()

print(numbers)


# Built-in Functions with Lists
numbers = [10, 20, 30, 40, 50]

print(len(numbers))     
print(max(numbers))      
print(min(numbers))      
print(sum(numbers))      
print(sorted(numbers))   


# Checking Items
print("apple" in fruits)
print("banana" not in fruits)


# Nested Lists
students = [
    ["Ali", 20],
    ["Sara", 21],
    ["Ahmed", 19]
]

print(students[0])
print(students[1][0])


