# a = 4 
# b = 2
# c = 1

# average = (a + b + c)/3
# print(average)


# a1 = 6
# b2 = 4
# c3 = 7

# average = (a1 + b2 + c3)/3
# print(average)


# def average(a, b, c):
#   d = (a + b + c)/3.0
#   # print(d)
#   return d

# o1 = average(3, 5, 1)
# o2 = average(4, 2, 1)

# print(o1)
# print(o2)


''' 
Functions Arguments & Return Values
'''

# def add(a, b, plus=0):
#   x = a + b + plus
#   return x

# c = add(3, 5, 2)
# print(c)

# c1 = add(b=5, a=3)
# print(c1)

'''Lambda Functions in Python'''

# square = lambda x: x*x

'''
As good as writing
def square(x):
  return x*x
'''
# sum = lambda x, y: x + y

'''
As good as writing
def sum(x,y):
    return x + y
'''

# print (square(3))
# print (sum(3, 62))

'''
Recursion in python
'''

'''
0 1 1 2 3 5 8 13
0 1 2 3 4 5 6 .......
fib(0) = 0
fib(1) = 1
fib(2) = fib(0) + fib(1)
fib(3) = fib(1) + fib(2)
fib(4) = fib(2) + fib(3)
fib(n) = fib(n-2) + fib(n-1)
'''
# def fib(n):
#   # Base case of recursion
#   if (n == 0 or n == 1):
#     return n 
  
#   return fib(n-2) + fib(n-1)

# print(fib(6))

# fib(4) + fib(5)
# fib(2) + fib(3) + fib(5)
# fib(0) + fib(1) + fib(3) + fib(5)
# 0 + 1 + fib(1) + fib(2) + fib(3) + fib(4)
# 0 + 1 + 1 + fib(0) + fib(1) + fib(1) + fib(2) + fib(4)
# 0 + 1 + 1 + 0 + 1 + 1 + fib(0) + fib(1) + fib(2) + fib(3)
# 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(0) + fib(1) + fib(1) + fib(2)
# 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + fib(0) + fib(1)
# 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1

'''
Modules and Pip
'''
# Two types of modules in Python
# - Built in Modules 
# - External Modules

# import math
# import os
# import mymodule
# import requests

# print(math.sqrt(16))
# mymodule.hello()
# r = requests.get("https://www.google.com")
# print(r.text)

'''

Variables Scope and Docstrings

'''

# def sum( a, b):
#   # a and b are local variables
#   c = a + b
#   z = 1 # It creates a local variable called z which is destroyed after this function returns
#   return c

# def greet():
#   z = 32 # Local Variable
#   print("Hello")


# z = 8  # z is a global variable
# print(sum(4, 6))
# print(z)

'''Global keyword'''

def sum(a, b):
  print("Hey I am summing")
  c = a + b
  global z # Please modify global z
  z = 0 # this will refer to global z and not create a local variable
  return c 
z = 3
print(sum(3, 12))
print(z)