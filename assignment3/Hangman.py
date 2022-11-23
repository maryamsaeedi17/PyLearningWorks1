import random

word_bank=["ocean", "bee", "fruit", "smell", "ship", "bike", "flower", "children", "sky", "night"]



u_error=0

true_chars=[]
false_chars=[]

x=random.randint(0,len(word_bank)-1)
word=word_bank[x]


while u_error<6:
    st=1

    for i in range(len(word)):
        if word[i] in true_chars:
            print(word[i], end=" ")
        else:
            print("-", end=" ")
            st=0
            

    if st==1:
        print("===> You win!")
        break



    u_char=input("Please write your guess: ").lower()
    if u_char in true_chars:
            print("Please guess a new letter..")


    if len(u_char)==1:
        if u_char in word:
            true_chars.append(u_char)
        else:
            false_chars.append(u_char)
            u_error+=1
    else:
        print("INVALID INPUT! Please enter a letter: ")

    if u_error==6:
        print("Game Over!")                

    
