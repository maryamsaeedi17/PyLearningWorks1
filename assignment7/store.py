import qrcode

PRODUCTS=[]
temp=[]

def read_from_database():
    d=open("database.txt","r")

    for line in d:
        res=line.split(",")
        my_dict={"code":res[0],"name":res[1],"price":res[2],"count":res[3].strip()}
        PRODUCTS.append(my_dict)
    #temp=PRODUCTS
    d.close()

def write_to_database():
    d = open("database.txt", "w")
    for p in PRODUCTS:
        d.write(str(p["code"])+","+str(p["name"])+","+str(p["price"])+","+str(p["count"]))

    print("Data saved successfully.👌")

    d.close()

def menu():
    print("1-Add")
    print("2-Edit")
    print("3-Remove")
    print("4-Search")
    print("5-Show list")
    print("6-Buy")
    print("7-Make QRcode")
    print("8-Save changes")
    print("9-Exit")             

def add():
    code=input("Please enter code:")
    name=input("Please enter name:")
    price=input("Please enter price:")
    count=input("Please enter count:")
    new_product={"code":code,"name":name,"price":price,"count":count}
    PRODUCTS.append(new_product)
    print("Successfully added!")
    #print(PRODUCTS)



def edit():
    code=input("Please enter the intended product code:")
    
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]["code"]==code:    
            x=i
            print("which field do you want to edit? \n 1-name \n 2-price \n 3-count")
            ch=int(input("Enter your choice:"))
            new_data=input("Please enter the new data:")
            if ch==1:
                PRODUCTS[x]["name"]=new_data
                print("Successfully edited!")
            elif ch==2:
                PRODUCTS[x]["price"]=new_data
                print("Successfully edited!")
            elif ch==3:
                PRODUCTS[x]["count"]=new_data
                print("Successfully edited!")
            else:
                print("Incorrect choice!!")
            break
    else:
        print("Not found!")


def remove():
    code=input("Please enter the intended product code:")
    for product in PRODUCTS:
        if product["code"]==code:
            PRODUCTS.remove(product)
            print("Successfully removed..")
            break
    else:
        print("Not found!")

def search():
    user_input=input("Type your keyword:")
    for product in PRODUCTS:
        if product["code"]==user_input or product["name"]==user_input:
            print(product["code"], "\t\t", product["name"],"\t\t",product["price"])
            break
    else:
        print("Not found!")                    
 

def show_list():
    print("code \t\t name \t\t price \t\t count")
    for product in PRODUCTS:
        print(product["code"], "\t\t", product["name"],"\t\t",product["price"],"\t\t",product["count"].strip())

def buy():
    factor=[]
    Total_cost=0
    while True:
        code=input("Please enter the product code to buy or type exit:")
        if code=="exit":
            break
        for product in PRODUCTS:
            if product["code"]==code:
                num=int(input("Please enter the number of product:"))
                if int(product["count"])<num:
                    print("Not enough stock!!")
                else:
                    product["count"]=int(product["count"])-num
                    cost=int(product["price"])*num
                    buy_dict={"c":product["code"],"n":product["name"],"number":num,"price":cost}   
                    factor.append(buy_dict)
                break
        else:
            print("Not found!")
    
    print("===================================================")
    print("code \t\t name \t\t number \t\t price")
    for product in factor:
        print(product["c"], "\t\t", product["n"],"\t\t", product["number"] , "\t\t" ,product["price"])
        Total_cost+=product["price"]
    print("===================================================")
    print("Total cost:" , Total_cost , "\n")
    print("🌻 Thanks for your shopping! 🌻 \n")



def make_qrcode():
    code=input("Please enter the intended product code:")
    for product in PRODUCTS:
        if product["code"]==code:
            q=qrcode.make(product["code"] + "-" + product["name"] + "-" +product["price"])
            q.save("product info to qrcode.png")
            print("QRcode successfully made!")
            break
    else:
        print("Not found!")



print("🌻 Welcome to Maryam Store 🌻")
print("Please wait, database is loading...")  
read_from_database()
print("Data loaded.")
#print(PRODUCTS)

while True:
    menu()
    choice=int(input("Please enter your choice:"))
    if choice==1:
        add()
    elif choice==2:
        edit()
    elif choice==3:
        remove()
    elif choice==4:
        search()
    elif choice==5:
        show_list()
    elif choice==6:
        buy()
    elif choice==7:
        make_qrcode()
    elif choice==8:
        write_to_database()
    elif choice==9:
        write_to_database()
        exit(0)
    else:
        print("❌Incorrect input!❌")    



