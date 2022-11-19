name=input("Please enter your name:")
family=input("Please enter your family:")

n=0
s=0

while True:

    score=input("Please enter the studen's score or type end for end:")
    if score=="end":
        break

    else:
        s=s+float(score)
        n=n+1

ave=s/n
print("Dear", name, family, ",Your average is:", ave)