a=int(input("Enter any number: "))
b=int(input("Enter any number: "))
c=int(input("Enter any number: "))

if a>=b and a>=c:
    print(a, " is greater.")
elif b>=a and b>=c:
    print(b, " is greater.")
else:
    print(c, "is greater.")