# Program to print multiplication table from 1 to 10 for a given number

# Get input from the user
number = int(input("Enter a number to see its multiplication table: "))


print(f"\nMultiplication table for {number}:")
print("-" * 20)

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
