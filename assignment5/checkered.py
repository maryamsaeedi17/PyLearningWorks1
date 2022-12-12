
def checkerd_sheet(n,m):
    print("let's print a checkered", n , "×" , m , "sheet!")

    for i in range(n):
        if i%2==0:
            for j in range(m):
                if j%2==0:
                    print("*", end=" ")
                else:
                    print("#", end=" ")
            print()        
        else:
            for j in range(m):
                if j%2==0:
                    print("#", end=" ")
                else:
                    print("*", end=" ")
            print()   

n=int(input("Please enter number of rows:"))
m=int(input("Please enter number of coloumns:"))

checkerd_sheet(n,m)