def generate_rug(n):
    number = n//2
    roundednumber = number +1
    a = number
    counter = 0
    list1 = []
    imj=["⚪","🟡","🟠","🔴","🟢","🔵","🟣","🟤","⚫"]
    for i in range(n):
        list1.append('')
    for i in range(roundednumber):
        if a == 0:
            list1[number] = imj[0]
            break
        (list1[counter],list1[(counter*-1)-1]) = imj[a%9],imj[a%9]
        a-=1
        counter+=1
            
    howmanyleft = 0
    emptylist = list1.copy()
    list1 =[]
    list1.insert(0,emptylist)
            
    for i in range(number):
        emptylist = emptylist.copy()
        #print(howmanyleft)
        for i in range(howmanyleft+1):
            (emptylist[number-i],emptylist[number+i]) = imj[(number-i+1)%9], imj[(number-i+1)%9]
        
        list1.insert(0,emptylist)
        list1.append(emptylist)    
        howmanyleft+=1
    
        # if howmanyleft >number:
        #     break

    for i in range(n):
        for j in range(n):
           print(list1[i][j], end=" ")
        print()

n=int(input("Please enter an odd number to make an n*n rug:"))
while True:
    if n%2==0:
        n=int(input("Sorry! Please enter an odd number:"))
        if n%2!=0:
            generate_rug(n)
            break
    else:
        generate_rug(n)
        break
