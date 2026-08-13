import random



def display_board(slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9):
    print("", slot1, "|", slot2, "|", slot3)
    print("---|---|---")
    print("", slot4, "|", slot5, "|", slot6)
    print("---|---|---")
    print("", slot7, "|", slot8, "|", slot9)

def check_winner(slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9):
    return (
        (slot1.isalpha() and slot1 == slot2 and slot2 == slot3) or # hoz 1
        (slot4.isalpha() and slot4 == slot5 and slot5 == slot6) or # hoz 2
        (slot7.isalpha() and slot7 == slot8 and slot8 == slot9) or # hoz 3
        (slot1.isalpha() and slot1 == slot4 and slot4 == slot7) or # ver 1
        (slot2.isalpha() and slot2 == slot5 and slot5 == slot8) or # ver 2
        (slot3.isalpha() and slot3 == slot6 and slot6 == slot9) or # ver 3
        (slot1.isalpha() and slot1 == slot5 and slot5 == slot9) or # diag 1
        (slot3.isalpha() and slot3 == slot5 and slot5 == slot7) #    diag 2
    )

def play_game():
    player = "X"
    moves = 0

    slot1 = " "
    slot2 = " " 
    slot3 = " " 
    slot4 = " "
    slot5 = " " 
    slot6 = " "
    slot7 = " " 
    slot8 = " " 
    slot9 = " " 

    print("--- Welcome to Tic-Tac-Toe! ---")
    display_board(slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9)

    while moves < 9:
        try:
            choice = int(input("Player " + player + " choose a space 1-9: "))
            if choice == 1 and not slot1.isalpha():
                slot1 = player
            elif choice == 2 and not slot2.isalpha():
                slot2 = player
            elif choice == 3 and not slot3.isalpha():
                slot3 = player
            elif choice == 4 and not slot4.isalpha():
                 slot4 = player
            elif choice == 5 and not slot5.isalpha():
                slot5 = player
            elif choice == 6 and not slot6.isalpha():
                slot6 = player
            elif choice == 7 and not slot7.isalpha():
                slot7 = player
            elif choice == 8 and not slot8.isalpha():
                    slot8 = player
            elif choice == 9 and not slot9.isalpha():
                    slot9 = player
            elif choice < 1 or choice > 9:
                print("pick a number 1 - 9")
                continue
            else:
                print("Space", choice, "is alredy taken")
                continue

            display_board(slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9)
            
            moves += 1
            if check_winner(slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9):
                 print("winner is ", player)
                 break
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