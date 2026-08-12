import random

is_playing = True
highscore = 0

while is_playing:
    winning_number = random.randint(1, 100)
    attempts = 0
    has_player_won = False

    while not has_player_won:
        try:
            guess = int(input("Guess a number (1 - 100): "))
            attempts += 1 

            if winning_number > guess:
                print("Higher")
            elif winning_number < guess:
                print("Lower")
            else: # This means that it matches
                print("Correct!!")
                has_player_won = True
        except ValueError:
            print("You guess must be a number.")

    print("You have won! You used", attempts, "to find the correct answer.")

    if highscore == 0 or highscore > attempts:
        highscore = attempts
        print("Congrats on the new highscore", highscore)
    else:
        print("Your highscore is", highscore)

    play_again = input("Do you want to play again (y/n)? ").strip().lower()

    is_playing = play_again in ["yes", "y"]

print("Thank you for playing!!!")