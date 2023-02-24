

karan_nbala = int(input(" Enter the highest numeric range : "))
karan_paiin = int(input(" Enter the lowest numeric range : "))
if karan_paiin > karan_nbala:
    help_box = karan_nbala
    karan_nbala = karan_paiin
    karan_paiin = help_box



while True:
    guide = int((karan_nbala + karan_paiin) / 2)
    print(guide)
    command_user = input(" guide ? up ? down ? or win ? : ")
    if command_user == "up":
        karan_paiin = guide

    elif command_user == "down":
        karan_nbala = guide

    elif command_user == "win":
        break        