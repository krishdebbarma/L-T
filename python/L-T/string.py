#creating empty strings

s1 = ""
s2 = str()
s3 = ''
print(type(s1), type(s2), type(s3))

#Dynamic input as string 
s4 = "hii"
print(s4, type(s4))

#Immutable
name = "Hello"
print(name)

#Indexing and slicing
name = "Krish"
print(name)
print(name[0])
print(name[-3])

#slicing 
print(name[:6])
print(name[2:4])
print(name[1:len(name):2])
print(name[::-1])
print(name[len(name)-1:0:-1])

#Concatenation 

name1 = "Madhu"
name2 = "Sudhan"
print(name1)
print(name2)
name = name1+name2
print(name)

# Repetation
sample = "sai"
new = sample*5
print(new)

# Membership 
name = "Kishor"
print("d" in name)
print("k" in name)
print("d" not in name)
print("r" not in name)

# Iteration
name = "World"
print("For in range")
for i in range(len(name)):
  print(name[i])

print("For Each")
for i in name:
  print(i)

# String Methods
s = "hello this is Naga sai"
print(s)
# Case
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())

# Searching
print(s.find('o'))
print(s.count('i'))
print(s.replace('ll','ee'))

# trimming
quote = "     Give Up     "
print(quote.strip())
print(quote.lstrip())
print(quote.rstrip())

# Split
thigs = "laptop,ipad,tablet,phone"
t = thigs.split(",")
print(t)

# join
about = ['I','Am','Lakhya','I','May','Be']
print(about)
about_lakhya = " Not ".join(about)
print(about_lakhya)

# Propertyh Checking
password = "helloThis19@me"
print(password[0].isalpha())
print(password[9].isalpha())
print(password[0].isalnum())
print(password[9].isalnum())
print(password[0].isdigit())
print(password[9].isdigit())

