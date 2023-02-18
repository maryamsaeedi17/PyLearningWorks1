import random

choices=["✋🏼", "🤚🏼"]
u_choice=input("Enter your choice ( ✋🏼 / 🤚🏼 ):")

c1_choice=random.choice(choices)
c2_choice=random.choice(choices)

if u_choice==c1_choice==c2_choice:
    print("No winner!")
elif u_choice==c1_choice!=c2_choice:
    print("Computer2 won.")
elif u_choice==c2_choice!=c1_choice:
    print("Computer1 won.")
elif u_choice!=c1_choice==c2_choice:
    print("You win! 🎉")