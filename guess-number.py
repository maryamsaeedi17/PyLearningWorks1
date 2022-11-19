import random

a=0
b=0
computer_number=random.randint(10,40)
print("You have only 10 chances!")
for i in range(10):
    user_number=int(input("Please enter your guess(an integer between 10 and 40):"))
    b=b+1
    if computer_number==user_number:
        print("You win!")
        print("Number of your guess:",b)
        a=1
        break
    elif computer_number>user_number:
        print("Go up")
    else:
        print("Go down.")

if a==0:
    print("GAME OVER!!")            
    

