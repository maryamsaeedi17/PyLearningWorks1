from mediaclass import Media
from filmclass import Film
from seriesclass import Series
from documentaryclass import Documentary
from clipclass import Clip

MEDIA=[]

def read_from_database():
    d=open("movie.txt","r")

    for line in d:
        res=line.split(",")
        #my_obj={"code":res[0],"name":res[1],"price":res[2],"count":res[3].strip()}
        if len(res)==10:
            if res[0]=="film":
                my_obj=Film(res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7])
            elif res[0]=="series":
                my_obj=Series(res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7],res[8])
            elif res[0]=="documentary":
                my_obj=Documentary(res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7])
            else:
                my_obj=Clip(res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7],res[9])
            MEDIA.append(my_obj)
    #temp=PRODUCTS
    d.close()

def write_to_database():
    d = open("movie.txt", "w")
    for m in MEDIA:
        if m.type=="film" or m.type=="documentary":
            d.write(str(m.type) + "," + str(m.name) + "," + str(m.director) + "," + str(m.imdb_score) + "," + str(m.url) + "," + str(m.duration)+ "," + str(m.casts) + "," + str(m.productionyear) + ",1,---"+"\n")
        elif m.type=="series":
            d.write(str(m.type) + "," + str(m.name) + "," + str(m.director) + "," + str(m.imdb_score) + "," + str(m.url) + "," + str(m.duration)+ "," + str(m.casts) + "," + str(m.productionyear) + "," + str(m.episodnumber) + ",---"+"\n")
        else:
            d.write(str(m.type) + "," + str(m.name) + "," + str(m.director) + "," + str(m.imdb_score) + "," + str(m.url) + "," + str(m.duration)+ "," + str(m.casts) + "," + str(m.productionyear) + ",1," + str(m.genre)+"\n")
        #d.write(str(p["code"])+","+str(p["name"])+","+str(p["price"])+","+str(p["count"]))
    
    print("Data saved successfully.👌")

    d.close()


def menu():
    print("1-Add")
    print("2-Edit")
    print("3-Remove")
    print("4-Search")
    print("5-Advanced Search")
    print("6-Show list")
    print("7-Show a media's info")
    print("8-Download")
    print("9-Save changes")
    print("10-Exit") 
    print()


def add():
    type=input("Enter type of media: ")
    name=input("Enter name of media: ")
    director=input("Enter director of media: ")
    imdb_score=input("Enter IMDB score of media: ")
    url=input("Enter uniform resource locator of media: ")
    duration=input("Enter duration of media: ")
    casts=input("Entre casts of media(separate with |): ")
    production_year=input("Enter production year of media: ")
    if type=="film":
        new_film=Film(type,name,director,imdb_score,url,duration,casts,production_year)
        MEDIA.append(new_film)
    elif type=="documentary":
        new_documentary=Documentary(type,name,director,imdb_score,url,duration,casts,production_year)
        MEDIA.append(new_documentary)
    elif type=="series":
        episod_number=input("Enter number of episodes of series: ")
        new_series=Series(type,name,director,imdb_score,url,duration,casts,production_year,episod_number)
        MEDIA.append(new_series)
    else:
        genre=input("Enter genre of clip:")
        new_clip=Clip(type,name,director,imdb_score,url,duration,casts,production_year,genre)
        MEDIA.append(new_clip)


def edit():
    name=input("Please enter the intended media name:")
    
    for i in range(len(MEDIA)):
        if MEDIA[i].name==name:    
            x=i
            print("which field do you want to edit? \n 1-director \n 2-url")
            ch=int(input("Enter your choice:"))
            new_data=input("Please enter the new data:")
            if ch==1:
                MEDIA[x].director=new_data
                print("Successfully edited!")
            elif ch==2:
                MEDIA[x].url=new_data
                print("Successfully edited!")
            else:
                print("Incorrect choice!!")
            break
    else:
        print("Not found!")



def remove():
    name=input("Please enter the intended media name:")
    for media in MEDIA:
        if media.name==name:
            MEDIA.remove(media)
            print("Successfully removed..")
            break
    else:
        print("Not found!")


def search():
    user_input=input("Type your keyword:")
    for media in MEDIA:
        if media.name==user_input or media.director==user_input:
            print(media.type, "\t\t", media.name, "\t\t", media.director,"\t\t",media.imdb_score, "\t\t" , media.url , "\t\t", media.casts , "\t\t", media.productionyear)
            break
    else:
        print("Not found!")


def advanced_search():
    i=int(input("Enter minimum time(in second): "))
    e=int(input("Enter maximum time(in second): "))
    n=0
    for media in MEDIA:
        if i<=int(media.duration)<=e:
            media.showinfo()
            n+=1
    if n==0:
        print("Not found any media with duration beetwin" , i , "and" ,e , "seconds!")



def show_list():
    print("name \t   director \t    IMDBscore \t duration \t\t casts  \t\t production year ")
    print("************************************************************************************************")
    for media in MEDIA:
        print(media.name, "\t\t", media.director,"\t\t",media.imdb_score,"\t\t", media.duration,"\t\t", media.casts ,"\t\t",media.productionyear.strip())
        print("----------------------------------------------------------------------------------------------------")






#print("🎦⏮⏩⏪⏭⏺⏹⏸▶🎞🎭📽🎬🎥⏳ Welcome to video media management program 🌻")
print("🎭🎞 Welcome to video media management program 🎞🎭")
print("Please wait, database is loading...")  
read_from_database()
print("Data loaded.")
#print(MEDIA)

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
        advanced_search()    
    elif choice==6:
        show_list()
    elif choice==7:
        na=input("\n Pleas enter media's name: ")
        for m in MEDIA:
            if m.name==na:
                m.showinfo()

    elif choice==8:
        na=input("\n Pleas enter media's name: ")
        for m in MEDIA:
            if m.name==na:
                m.download()
    elif choice==9:
        write_to_database()
    elif choice==10:
        write_to_database()
        exit(0)
    else:
        print("❌Incorrect input!❌")    

