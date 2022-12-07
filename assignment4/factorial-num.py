n=int(input("Please enter an integer number:"))

factorial=1

if n==1 or n==2:
    print("Yes")

else:
    for i in range(1,n):
        if n%i==0:
            factorial*=i
        else:
            break
        if n==factorial:
            print("Yes")
            break
    #   else:
    #       print("No") 
    if n!=factorial:
        print("No")

           
