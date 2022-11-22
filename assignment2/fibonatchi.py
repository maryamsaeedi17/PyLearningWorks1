n=int(input("Please enter the number of  sentences of your Fibonatchi's sequence:"))

a=1
b=0

for i in range(n):
    r=a+b
    print(r)
    a=b
    b=r
    