n=int(input("Please enter the number of your list's elements:"))

main_list=[]
unrepeated_list=[]

for i in range(n):
    #num=int(input("Please enter the list's numbers:"))
    data=input("Please enter the list's elements:")
    main_list.append(data)

for i in range(n):
    if main_list[i] not in unrepeated_list:
        unrepeated_list.append(main_list[i])

print(unrepeated_list)   