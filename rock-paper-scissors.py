import random

C_score=0
U_score=0

print("For quite the game, please enter exit.")

while C_score<5 and U_score<5:
    x= random.randint(1,3)
    if x==1:
        C_choice="rock"
    elif x==2:
        C_choice="paper"
    else:
        C_choice="scissors"

    U_choice=input("Please enter your choice:") 

    print("Computer choice is:", C_choice)
    print("User choice is:", U_choice)

    if U_choice=="exit":
        break

    if C_choice=="rock" and U_choice=="paper":
        U_score=U_score+1
        print("User score is:", U_score, ", Computer score is:", C_score)
    elif C_choice=="rock" and U_choice=="scissors":
        C_score=C_score+1
        print("User score is:", U_score, ", Computer score is:", C_score)
    elif C_choice=="rock" and U_choice=="rock":
        print("User score is:", U_score, ", Computer score is:", C_score)

    elif C_choice=="paper" and U_choice=="rock":
        C_score=C_score+1
        print("User score is:", U_score, ", Computer score is:", C_score)
    elif C_choice=="paper" and U_choice=="scissors":
        U_score=U_score+1
        print("User score is:", U_score, ", Computer score is:", C_score)
    elif C_choice=="paper" and U_choice=="paper":
        print("User score is:", U_score, ", Computer score is:", C_score)

    elif C_choice=="scissors" and U_choice=="paper":
        C_score=C_score+1
        print("User score is:", U_score, ", Computer score is:", C_score)
    elif C_choice=="scissors" and U_choice=="rock":
        U_score=U_score+1
        print("User score is:", U_score, ", Computer score is:", C_score)
    elif C_choice=="scissors" and U_choice=="scissors":
        print("User score is:", U_score, ", Computer score is:", C_score)

if C_score>U_score:
    print("Winner: Computer")
elif C_score<U_score:
    print("Winner: You!, Congratulations!")
else:
    print("Your score is equal to computer's score.")                        






