a=float(input("Please enter first side:"))
b=float(input("Please enter second side:"))
c=float(input("Please enter third side:"))

if a<b+c and b<a+c and c<a+b:
    print("Yes!")
else:
    print("No")
    