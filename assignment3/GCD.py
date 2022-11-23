print("Please enter 2 positive integers:")
n1=int(input("First number: "))
n2=int(input("Second number: "))

if n1>n2:
    temp=n1
    n1=n2
    n2=temp

for i in range(1,n1+1):
    if n1%i==0 and n2%i==0:
        gcd=i

print("The G.C.D. of your numbers is: ", gcd)   
