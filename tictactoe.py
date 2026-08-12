import random



def display_board(slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9):
    print("", slot1, "|", slot2, "|", slot3)
    print("---|---|---")
    print("", slot4, "|", slot5, "|", slot6)
    print("---|---|---")
    print("", slot7, "|", slot8, "|", slot9)

def check_winner(slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9):
    return (
        (slot1 == slot2 and slot2 == slot3) or # hoz 1
        (slot4 == slot5 and slot5 == slot6) or # hoz 2
        (slot7 == slot8 and slot8 == slot9) or # hoz 3
        (slot1 == slot4 and slot4 == slot7) or # ver 1
        (slot2 == slot5 and slot5 == slot8) or # ver 2
        (slot3 == slot6 and slot6 == slot9) or # ver 3
        (slot1 == slot5 and slot5 == slot9) or # diag 1
        (slot3 == slot5 and slot5 == slot7) #    diag 2
    )

def play_game():
    player = "X"
    moves = 0

    slot1 = ""
    slot2 = "" 
    slot3 = "" 
    slot4 = ""
    slot5 = "" 
    slot6 = ""
    slot7 = "" 
    slot8 = "" 
    slot9 = "" 

    print("--- Welcome to Tic-Tac-Toe! ---")
    display_board(slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9)

    while moves < 9:
        try:
            choice = int(input("Player " + player + " choose a space 1-9: "))
            if choice == 1 and slot1 == "":
                slot1 = player
            elif choice == 2 and slot2 == "":
                slot2 = player
            elif choice == 3 and slot3 == "":
                slot3 = player
            elif choice == 4 and slot4 == "":
                 slot4 = player
            elif choice == 5 and slot5 == "":
                slot5 = player
            elif choice == 6 and slot6 == "":
                slot6 = player
            elif choice == 7 and slot7 == "":
                slot7 = player
            elif choice == 8 and slot8 == "":
                    slot8 = player
            elif choice == 9 and slot9 == "":
                    slot9 = player
            elif choice < 1 or choice > 9:
                print("pick a number 1 - 9")
                break
            else:
                print("Space", choice, "is alredy taken")
            
            moves += 1
            if check_winner(slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9):
                 print("winner is ", player)
            else:
                if player == "X":
                      player = "O"
                else:
                     player = "X"
        except ValueError:
            print("must be a number 1 - 9")

    if moves > 9:
         print("Game is a tie!")


while True:
    play_game()
    play_again = input("\nPlay Again? (y / n) ").strip().lower()
    if play_again == 'n':
        break