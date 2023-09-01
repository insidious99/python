# Write a program that asks the user to enter a positive integer n 
# and prints a triangle pattern of numbers.

n = int(input("Enter a number: "))

for j in range(1, n + 1):
    for i in range(1, j + 1):
        print(i, end = "")
    print()
