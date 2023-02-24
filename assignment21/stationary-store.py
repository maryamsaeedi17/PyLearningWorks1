import sqlite3

def menu():
    print("1-Add")
    print("2-Edit")
    print("3-Remove")
    print("4-Search")
    print("5-Show list")
    print("6-Buy")
    print("7-Save changes")
    print("8-Exit")  

def load_database():
    global connection
    global my_cursor
    connection= sqlite3.connect("store-goods.db")
    my_cursor=connection.cursor()

def add():
    name=input("Enter the name of the new product:")
    price=input("Enter the price of the new product:")
    count=input("Enter the count of the new product:")
    my_cursor.execute(f"INSERT INTO goods(Name, Price, Count) VALUES ('{name}', '{price}', '{count}')")
    connection.commit()
    print("New product added successfully.")

def edit():
    id=input("Please enter the intended product ID:")
    for data in my_cursor.execute(f"SELECT * FROM goods WHERE Id={id}"):
        print(data)
    print("which field do you want to edit? \n 1-name \n 2-price \n 3-count")
    ch=int(input("Enter your choice:"))
    new_data=input("Please enter the new data:")
    if ch==1:
        my_cursor.execute(f"UPDATE goods SET Name='{new_data}' WHERE Id='{id}' ")        
        print("Successfully edited!")
    elif ch==2:
        my_cursor.execute(f"UPDATE goods SET Price='{new_data}' WHERE Id='{id}' ")
        print("Successfully edited!")
    elif ch==3:
        my_cursor.execute(f"UPDATE goods SET Count='{new_data}' WHERE Id='{id}' ")
        print("Successfully edited!")
    else:
        print("Incorrect choice!!")
    
    connection.commit()

def remove():
    id=input("Please enter the intended product ID:")
    my_cursor.execute(f"DELETE FROM goods WHERE Id={id}")
    connection.commit()
    print("Successfully removed..")

def search():
    user_input=input("Type your keyword:")
    for data in my_cursor.execute(f"SELECT * FROM goods WHERE Id={user_input} OR Name={user_input}"):
        print(data)

def show_list():
    print("ID.   Name   Price   Count")
    print("===============================")
    for data in my_cursor.execute("SELECT * FROM goods"):
        print(data)

def buy():
    factor=[]
    Total_cost=0
    while True:
        id=input("Please enter the product ID to buy or type exit:")
        if id=="exit":
            break
        n=int(input("Enter the number to buy:"))
        count=my_cursor.execute(f"SELECT Count FROM goods WHERE Id={id}")
        c=int(count.fetchone()[0])
        if c<n:
            print("Not enough stock!!")
        else:
            new_count=c-n
            my_cursor.execute(f"UPDATE goods SET Count='{new_count}' WHERE Id='{id}'")
            price=my_cursor.execute(f"SELECT Price FROM goods WHERE Id={id}")
            p=float(price.fetchone()[0])
            cost=p*n
            name=my_cursor.execute(f"SELECT Name FROM goods WHERE Id={id}")
            product_name=str(name.fetchone()[0])
            buy_dict={"c":id,"n":product_name,"number":n,"price":cost}   
            factor.append(buy_dict)

    connection.commit()

    print("===================================================")
    print("code \t\t name \t\t number \t\t price")
    for product in factor:
        print(product["c"], "\t\t", product["n"],"\t\t", product["number"] , "\t\t" ,product["price"])
        Total_cost+=product["price"]
    print("===================================================")
    print("Total cost:" , Total_cost , "\n")
    print("🌻 Thanks for your shopping! 🌻 \n")



print("🌻 Welcome to our stationary store. 🌻")
print("Please wait, database is loading... ⏳")  
load_database()
print("Data loaded.🎨📚")

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
        connection.commit()
    elif choice==8:
        connection.commit()
        exit(0)
    else:
        print("❌Incorrect input!❌")    



