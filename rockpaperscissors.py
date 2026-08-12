import random

player_wins = 0
computer_wins = 0
ties = 0

choices = ['rock', 'paper', 'scissors']

def determine_winner(player_choice, computer_choice):
    if(player_choice == computer_choice):
        return 'tie'
    elif((player_choice == 'rock' and computer_choice == 'scissors')):
        return 'player'
    elif(player_choice == 'paper' and computer_choice == 'rock'):
        return 'player'
    elif(player_choice == 'scissors' and computer_choice == 'paper'):
        return 'player'
    else:
        return 'computer'

def display_results(player, computer, winner):
    print("p: " + player, "c: " + computer, "winner: " + winner, sep="\n")


while True:
    player_choice = input("rock, paper, scissors? ").strip().lower()

    if player_choice in choices:
        computer_choice = random.choice(choices)

        winner = determine_winner(player_choice, computer_choice)
        display_results(player_choice, computer_choice, winner)

        if (winner == 'tie'):
            ties += 1
        elif(winner == "player"):
            player_wins += 1
        else:
            computer_wins += 1

        print("wins", "------", "player: " + str(player_wins), "computer: " + str(computer_wins), "ties: " + str(ties), sep="\n")
        play_again = input("\nPlay Again? (y / n) ").strip().lower()
        if play_again == 'n':
            break
    else: 
        print("please choose again.")