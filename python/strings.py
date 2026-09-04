text = "Python Programming"

# Length
print(len(text))         

# Access characters
print(text[0])            
print(text[-1])           

# Slicing
print(text[0:6])      
print(text[:6])          
print(text[7:])           

# Change case
print(text.lower()) 
print(text.upper())      

# Replace text
print(text.replace("Python", "Java"))

# Check contents
print("Python" in text)  


# Joining & formatting
first = "Abeera"
last = "Ather"

full_name = first + " " + last
print(full_name)
age = 19
print(f"My name is {first} and I am {age} years old.")

# String Methods
text =   "Hello world"
print(text.strip())         
print(text.split())  
print(text.startswith("h"))
print(text.endswith("d"))
print(text.find("world"))
print(text.count("l"))