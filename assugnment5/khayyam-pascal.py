def khayyam_pascal_tiangle(n):
    if n<=0:
        n=int(input("Please enter a positive integer:"))

    ur=[1] #ul=upper raw
    lr=[1]  #ll=lower raw 

    for i in range(n-1):
        ur.append(0)
        lr.append(0)

    for i in range(n):
        print(lr[0] , end=" ")
        for j in range(1,i+1):
            lr[j]=ur[j]+ur[j-1]
            if lr[j]!=0:
                print(lr[j],end=" ")
        print()

        for i in range(n):
            ur[i]=lr[i]

                     
n=int(input("Please enter your desire number to calculate the Khayyam-Pascal's triangle:"))
khayyam_pascal_tiangle(n)    