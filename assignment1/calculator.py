import math

print("Wellcome to Mary calculator!")
print("Two variable operators:")
print("+:sum")
print("-:sub")
print("*:mul")
print("/:div")
print("One variable operators:")
print("sqrt: square root")
print("sin")
print("cos")
print("tan")
print("cot")
print("fact: factorial")

print("Please enter your operator:")
op=input()

if op=="+": 
    a=float(input("Please enter first number:"))
    b=float(input("Please enter second number:"))
    r=a+b

    print(r)

elif op=="-":
    a=float(input("Please enter first number:"))
    b=float(input("Please enter second number:"))
    r=a-b

    print(r)

elif op=="*":
    a=float(input("Please enter first number:"))
    b=float(input("Please enter second number:"))
    r=a*b
    
    print(r) 

elif op=="/":
    a=float(input("Please enter first number:"))
    b=float(input("Please enter second number:"))
    if b==0:
        print("Cannot divide by zero!")
    else:
        r=a/b
    
        print(r)   

elif op=="sqrt":
    a=float(input("Please enter your number:"))
    if a<0:
        print("Square root for negative numbers isnot possible!")    
    else:
        r=math.sqrt(a)

        print(r)

elif op=="sin":
    d=float(input("Please enter your angle in degree:"))
    R=(d/180)*math.pi
    r=math.sin(R)

    print(r)

elif op=="cos":
    d=float(input("Please enter your angle in degree:"))
    R=d/180*math.pi
    r=math.cos(R)

    print(r)

elif op=="tan":
    d=float(input("Please enter your angle in degree:"))
    R=d/180*math.pi
    r=math.tan(R)

    print(r)

elif op=="cot":
    d=float(input("Please enter your angle in degree:"))
    R=d/180*math.pi
    r=1/math.tan(R)

    print(r)

elif op=="fact":
    a=int(input("Please enter your integer number:"))
    r=math.factorial(a)

    print(r)
