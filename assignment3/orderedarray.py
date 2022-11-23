l=int(input("Please enter the length of your array:"))

array=[]

for i in range(l):
    number=int(input("Please enter numbers of your array:"))
    array.append(number)

for i in range(l-1):
    if array[i]>array[i+1]:
        print("Your array is not ordered.")
        break
    else:
        if i+1==l-1:
            print("Your array is ordered.")