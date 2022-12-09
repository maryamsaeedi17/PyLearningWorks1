def diamond(n):

    for i in range(n):
        for j in range(n-1-i):
            print(" " , end=" ")
        for k in range(2*i+1):
            print("⁛" , end=" ")
        print()

    for i in range(n-1):
        for j in range(i+1):
            print(" " , end=" ")
        for k in range(2*n-1-2*(i+1)):
            print("⁛" , end=" ")
        print()

n=int(input("Please enter a number to draw a diamond:"))
diamond(n)