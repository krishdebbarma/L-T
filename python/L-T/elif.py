# # if( condition ):
#      # Code
# # if( True ):
# #.   code will execute
# a = 10
# if(a == 20):
#     print("Yes You are Right")

# # IF... Else
# # if - If Condition fails then Else will be executed automatically
# a = 11
# if(a == 10):
#     print("Hello World")
# else:
#     print("hey World")

# # Else If - elif
# # if -> if conditon falis then elif will be checked if all fails then else will be executed
# a = 10
# if(a>10):
#     print("Jukega nai")
# elif(a<10):
#     print("Jukega")
# else:

#     print("Both are Same Pushpa")


# #Topper
# marks = int(input("Enter a number"))
# if marks == 100:
#     print("Topper")
# elif marks >= 35:
#     print("Pass")
# else:
#     print("Fail")


#Calculator

num1 = int(input("Enter the  number-1: "))
num2 = int(input("Enter the number-2: "))

op = int(input("Enter the option 1. Addition 2. Substraction 3. Multiplication 4. Division: "))
if(op ==1):
    print(num1+num2)
elif(op == 2):
    print(num1-num2)
elif(op == 3):
    print(num1*num2)
elif(op == 4):
    print(num1/num2)
else:
    print("Please enter the Valid Option")