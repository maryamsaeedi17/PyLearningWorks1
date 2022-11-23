n=int(input("Please enter your snake's length:"))

for i in range(n):
    if i%2==0:
        print("*", end="")
    else:
        print("#", end="")    