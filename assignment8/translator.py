import os.path
from os import path
import gtts
from playsound import playsound


def read_from_file():
    global words_bank
    f=open("translate.txt","r")
    words_bank=[]
    temp=f.read().split("\n")
    for i in range(0,len(temp),2):
        my_dict={"en":temp[i],"fa":temp[i+1]}
        words_bank.append(my_dict)

    f.close()


def english_to_persian():
    user_text=input("Enter your english text:").replace('.', ' *')
    user_words=user_text.split(" ")
    output=" "
    for user_word in user_words:
        for word in words_bank:
            if user_word==word["en"]:
                output=output+word["fa"]+" "
                break
        else:
            output=output+user_word+" "
    output=output.replace(" *",".")
    print("Translation:", output)

def persian_to_english():
    user_text = input("Enter persian text:").replace('.', ' *')
    user_words=user_text.split(" ")
    output=" "
    for user_word in user_words:
        for word in words_bank:
            if user_word==word["fa"]:
                output=output+word["en"]+" "
                break
        else:
            output=output+user_word+" "

    output=output.replace(" *",".")
    print("Translation:", output)

    s=gtts.gTTS(output,lang="en",slow=False)
    s.save("Tvoice.mp3")
    
    playsound("C:/Users/ara/Desktop/MyProjects1/PyLearningWorks1/assignment8/Tvoice.mp3")



def add_to_database():
    file_name=input("Please enter name of database(.txt) to add new word:")
    if path.exists(file_name):
        d = open("translate.txt", "a")
        new_word_en=input("Please enter your english word:")
        for word in words_bank:
            if new_word_en==word["en"]:
                print("This word is alredy in database!! \n")
                break
        else:
            new_word_fa=input("Please enter its translation in pesian:")
            d.write("\n"+new_word_en+"\n"+new_word_fa)
            print("New word added successfully. \n")
        d.close()

    else:
        print("File does not exist! \n")

    

def show_menu():
    print("🌎 Welcome to Maryam translator 🌏")
    print("1- Translate English to Persian")
    print("2- Translate Persian to English")
    print("3- Add a new word to database")
    print("4-Exit")


read_from_file()
#print(words_bank)
while True:
    show_menu()
    ch=int(input("Please enter your choice:"))
    if ch==1:
        english_to_persian()
    elif ch==2:
        persian_to_english()
    elif ch==3:
        add_to_database()
    elif ch==4:
        exit(0)
    else:
        print("❌ Incorrect input!! ❌")
