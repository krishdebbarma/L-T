# name = "Krish"
# name = '''Krish
# is a good person'''
# name = 'Krish'

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])

# print(name[-1])
# print(name[-2])
# print(name[-3])
# print(name[-4])
# print(name[-5])


# print(name[-3+5])


'''String slicing and 
Indexing'''

# name = "Krish0123456789"

# print(name[0:3])
# print(name[2:-1]) # Same as name [2:4]

# # print(name[0:10:n]) # Skip n-1 characters
# print(name[0:10:1]) # Skip 0 Character
# print(name[0:10:2]) # Skip 1 Character

# print(name[:4]) # It will replace the empty number with 0 i.e name[0:4]
# print(name[1:]) # It will replace the second empty number with length -1 i.e name[1:15]


'''Strings Methods and Functions'''

#name = "krish debbarma" # Strings are immutable 

# name[0] = "R" # You can't change the string 
# Changing cases
#a = len(name)
#print(a)
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.title())

# Removing Whitespace

# text ="  hello world  " 
# print(text.strip()) # Output: "hello world" 
# print(text.lstrip())# Output: "hello world  " 
# print(text.rstrip())# Output: "  hello world"

# Finding and Replacing

# text = "Python is fun"

# print(text.find("is"))
# print(text.replace("fun", "awesome"))


# text = "Apples,Banana,Pineapples"

# print( text.split(","))
# print(",".join(['Apples', 'Bananas', 'Pineapples']))

# text ="Python123" 
# print(text.isalpha()) #Output:False 
# print(text.isdigit()) # Output: False 
# print(text.isalnum()) # Output: True 
# print(text.isspace()) # Output: False


'''String Formatting'''

# template = "Dear {}, You are awesome. Take this {}$ bag"
# a = "John"
# a1 = 1000
# b = "Jack"
# b1 = 1000
# c = "Marie"
# c2 = 300
# s1 = template.format(a, a1)
# print(s1)

# print(f"{a} you are awesome and take this {a1}$ bag")

# text = "Hello, Python!"
# print(len(text))

# print(ord('A'))  
# print(chr(65))

name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")