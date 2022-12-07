n=int(input("Please enter the number of your list's elements:"))

main_list=[]

for i in range(n):
    #num=int(input("Please enter the list's numbers:"))
    data=input("Please enter the list's elements:")
    main_list.append(data)

for i in range(n//2):
    temp=main_list[i]
    main_list[i]=main_list[n-1-i]
    main_list[n-1-i]=temp

print("The reversed list is:" , main_list)   