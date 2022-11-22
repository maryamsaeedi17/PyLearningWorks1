name=input("Please enter your name:")
family=input("Please enter your family:")

s1=float(input("Please enter your first score:"))
s2=float(input("Please enter your second score:"))
s3=float(input("Please enter your third score:"))

ave=(s1+s2+s3)/3

if ave>=17:
    print("Dear", name, family, ",Your average is:", ave, " ,Status: Great!")
elif ave<17 and ave>=12:
    print("Dear", name, family, ",Your average is:", ave, " ,Status: Normal")
elif ave<12:
    print("Dear", name, family, ",Your average is:", ave, " ,AStatus: Fail")
