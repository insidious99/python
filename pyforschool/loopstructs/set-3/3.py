# Write a program that asks the user to enter a positive integer n 
# and prints a right-angled triangle.

n = int(input("Enter the number: "))

for i in range(1, n + 1):
    print(" " * (n - i), end = "")
    for j in range(1, i + 1):
        print(j, end = "")
    print()
