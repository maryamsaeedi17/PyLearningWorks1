import random

while True:
    d=random.randint(1,6)
    if d==6:
        print("You won and you have one more chance!")
    else:
        print("You lost!")
        break    