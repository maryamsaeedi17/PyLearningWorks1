import pyfiglet
from termcolor import colored
import random
import time



def show():
    for row in game_board:
        for cell in row:
            print(cell, end=" ")
        print( )

def menu():
    print("1-Two player.")
    print("2-One Player and PC.")
    print("3-Exit.") 

def check_game_1(GB):
        if GB[0][0] == GB[0][1] == GB[0][2] == (colored("X", "red")) or GB[1][0] == GB[1][1] == GB[1][2] == (colored("X", "red")) or GB[2][0] == GB[2][1] == GB[2][2] == (colored("X", "red")) or GB[0][0] == GB[1][0] == GB[2][0] == (colored("X", "red")) or GB[0][1] == GB[1][1] == GB[2][1] == (colored("X", "red")) or GB[0][2] == GB[1][2] == GB[2][2] == (colored("X", "red")) or GB[0][0] == GB[1][1] == GB[2][2] == (colored("X", "red")) or GB[0][2] == GB[1][1] == GB[2][0] == (colored("X", "red")):
            print("Finish! Winner: Player1")
            end = time.time()
            d=int(end-start)
            print("Duration:", d ,"second")
            exit(0)
        elif GB[0][0] == GB[0][1] == GB[0][2] == (colored("O", "blue")) or GB[1][0] == GB[1][1] == GB[1][2] == (colored("O", "blue")) or GB[2][0] == GB[2][1] == GB[2][2] == (colored("O", "blue")) or GB[0][0] == GB[1][0] == GB[2][0] == (colored("O", "blue")) or GB[0][1] == GB[1][1] == GB[2][1] == (colored("O", "blue")) or GB[0][2] == GB[1][2] == GB[2][2] == (colored("O", "blue")) or GB[0][0] == GB[1][1] == GB[2][2] == (colored("O", "blue")) or GB[0][2] == GB[1][1] == GB[2][0] == (colored("O", "blue")):
            print("Finish! Winner: player2")
            end = time.time()
            d=int(end-start)
            print("Duration:", d ,"second")
            exit(0)
        elif GB[0][0]!= "_" and GB[0][1]!= "_" and GB[0][2]!= "_" and GB[1][0]!= "_" and GB[1][1]!= "_" and GB[1][2]!= "_" and GB[2][0]!= "_" and GB[2][1]!= "_" and GB[2][2] != "_":
            print("No winner! No loser!")
            end = time.time()
            d=int(end-start)
            print("Duration:", d ,"second")
            exit(0)

def check_game_2(GB):
        if GB[0][0] == GB[0][1] == GB[0][2] == (colored("X", "red")) or GB[1][0] == GB[1][1] == GB[1][2] == (colored("X", "red")) or GB[2][0] == GB[2][1] == GB[2][2] == (colored("X", "red")) or GB[0][0] == GB[1][0] == GB[2][0] == (colored("X", "red")) or GB[0][1] == GB[1][1] == GB[2][1] == (colored("X", "red")) or GB[0][2] == GB[1][2] == GB[2][2] == (colored("X", "red")) or GB[0][0] == GB[1][1] == GB[2][2] == (colored("X", "red")) or GB[0][2] == GB[1][1] == GB[2][0] == (colored("X", "red")):
            print("Finish! Winner: You")
            end = time.time()
            d=int(end-start)
            print("Duration:", d ,"second")
            exit(0)
        elif GB[0][0] == GB[0][1] == GB[0][2] == (colored("O", "blue")) or GB[1][0] == GB[1][1] == GB[1][2] == (colored("O", "blue")) or GB[2][0] == GB[2][1] == GB[2][2] == (colored("O", "blue")) or GB[0][0] == GB[1][0] == GB[2][0] == (colored("O", "blue")) or GB[0][1] == GB[1][1] == GB[2][1] == (colored("O", "blue")) or GB[0][2] == GB[1][2] == GB[2][2] == (colored("O", "blue")) or GB[0][0] == GB[1][1] == GB[2][2] == (colored("O", "blue")) or GB[0][2] == GB[1][1] == GB[2][0] == (colored("O", "blue")):
            print("Finish! Winner: PC")
            end = time.time()
            d=int(end-start)
            print("Duration:", d ,"second")
            exit(0)
        elif GB[0][0]!= "_" and GB[0][1]!= "_" and GB[0][2]!= "_" and GB[1][0]!= "_" and GB[1][1]!= "_" and GB[1][2]!= "_" and GB[2][0]!= "_" and GB[2][1]!= "_" and GB[2][2] != "_":
            print("No winner! No loser!")
            end = time.time()
            d=int(end-start)
            print("Duration:", d ,"second")
            exit(0)




title = pyfiglet.figlet_format("TicTacToe" , font = "slant")
print(title)

while True:
    menu()
    status=int(input("Please enter your choice:"))
    start = time.time()

    if status == 1:
        game_board = [["_", "_", "_"],
                      ["_", "_", "_"],
                      ["_", "_", "_"]]

        show()
        while True:
            print("Player1: ")

            while True :
                row = int(input("Please enter number of row of your choice : "))
                col = int (input("Please enter number of column of your choice : "))
                if 1<=row<=3 and 1<=col<=3 :
                    if game_board[row-1][col-1] == "_":
                        game_board[row-1][col-1] = (colored("X", "red"))
                        break
                    else :
                     print("Incorrect choice! Please select an empty place:")
                else :
                    print ("Invalid input! You can only choose 1 or 2 or 3.")

            show()
            check_game_1(game_board)

            print("Player2: ")
            while True :
                row = int(input("Please enter number of row of your choice: "))
                col = int (input("Please enter number of column of your choice : "))
                if 1<=row<=3 and 1<=col<=3 :
                    if game_board[row-1][col-1] == "_":
                        game_board[row-1][col-1] = (colored("O", "blue"))
                        break
                    else :
                        print("Incorrect choice! Please select an empty place:")
                else :
                    print ("Invalid input! You can only choose 1 or 2 or 3.")
            show()
            check_game_1(game_board)


    elif status == 2:
        game_board = [["_", "_", "_"],
                      ["_", "_", "_"],
                      ["_", "_", "_"]]

        show()
        while True:
            print("Your turn: ")

            while True :
                row=int(input("Please enter number of row of your choice : "))
                col=int (input("Please enter number of column of your choice : "))
                if 1<=row<=3 and 1<=col<=3 :
                    if game_board[row-1][col-1] == "_":
                        game_board[row-1][col-1] = (colored("X", "red"))
                        break
                    else :
                     print("Incorrect choice! Please select an empty place:")
                else :
                    print ("Invalid input! You can only choose 1 or 2 or 3.")

            show()
            check_game_2(game_board)

            print("PC:")
            while True :
                raw=random.randint(1, 3)
                col=random.randint(1, 3)
                if game_board[col-1][row-1] == "_":
                    game_board[col-1][row-1] = (colored("O", "blue"))
                    break
                else:
                    continue
            show()
            check_game_2(game_board)

    elif status == 3:
        exit(0)
    else:
        print("Wrong choice!(Please pay attention to menu.)")


