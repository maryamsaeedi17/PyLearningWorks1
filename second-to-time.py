total_s=int(input("Please enter your time in second:"))

h=total_s//3600
d=total_s%3600
m=d//60
s=d%60

print("Your time is", h,":",m,":",s)

