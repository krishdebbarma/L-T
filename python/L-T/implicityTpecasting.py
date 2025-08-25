# # implicit Type Casting -> Safe -> Low to High
# a = 20
# print(a,type(a))
# a = float(a) # -> implicit Type Casting -> float() Constructor
# print(a,type(a))

# # Explicit Type Casting -> Unsafe -> High to Low -> Data Loss May Occur
# b = 22.57
# print(b,type(b))
# b = int(b) # -> int() Constructor -> explicit Type Casting
# print(b,type(b))

# #Break
# for i in range(1,10):
#   print("Hello World",i)
#   if(i==7):
#     break

# #COntinue
# for i in range(1,10):
#   print("hi",i)
#   if(i==7):
#     continue 
#   print("bye bye",i)


#Bitwise Operators
#Bitwise AND
# print(6&8)
# print(5&6)

# #Bitwise OR
# print(6|8)
# print(5|6)


# #Bitwise XOR
# print(6^8)
# print(5^6)

# #Bitwise NOT
# print(~5)
# print(~-5)

# #Bitwise Right Shift 
# print(13>>1)
# print(13>>2)

# #Bitwise Left Shift
# print(6<<1)
# print(6<<2)
# print(6<<3)

#FInd whether a number is even or odd using arihtmetic operator

# num = 5 #int(input())
# if(num&1 == 0):
#   print("Even")
# else: 
#   print("Odd")

#Find whether the given number is power of two or not

#write a program to find the factorial of a number

# n = int(input(5))
# ans = 1
# for i in range(1,n+1):
#   ans = ans*i
# print(ans)


#find whether a number is palindrome or not

# num = 78987 #int(input())
# rev = 0
# temp = num
# while(temp != 0):
#   rem = temp%10
#   rev = rev*10 + rem
#   temp = temp//10
# if(rev == num):
#   print("It is a palidrome")
# else:
#   print("It is not a palidrome")


#Q Write a python program to find wehther a number is prime number or not

n = 31 #int(input())
is_prime = True
if (n<=1):
  print("Not prime")
else:
  for i in range (2,(n//2)+1):
    if n%i == 0:
      is_prime == False
      break
if (is_prime == True):
  print("Prime")
else:
  print("non prime")