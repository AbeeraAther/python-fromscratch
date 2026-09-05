# if statement
age = 20

if age >= 18:
    print("You are an adult")

# if-else statement  
age = 15

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

#if-elif-else statement
marks = 75

if marks >= 80:
    print("A Grade")
elif marks >= 60:
    print("B Grade")
elif marks >= 40:
    print("C Grade")
else:
    print("Fail")

#Nested-if statement
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("You are underage")     