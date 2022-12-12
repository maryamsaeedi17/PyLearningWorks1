
def muliplication_table(n,m):
    print("Now, we have a" , n , "×" , m , "multiplication table:")

    for i in range(n+1):
        if i==0:
            for j in range(m+1):
                if j==0:
                    print("×", end=" ")
                else:
                    print(j,end=" ")   
            print()        
        else:
            for j in range(m+1):
                if j==0:
                    print(i, end=" ")
                else:
                    print(i*j, end=" ")
            print()   


n=int(input("Please enter the first number:"))
m=int(input("Please enter the second number:"))        

muliplication_table(n,m)