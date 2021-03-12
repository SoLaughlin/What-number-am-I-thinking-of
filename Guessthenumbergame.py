# A simple, what number am I thinking of game.
import random

# Strings and inputs for welcoming a user to the game and asking for their name.

print("Hello!")
user_name = input("What is your name?: ")

introduction_text = f"Okay {user_name}, lets play a game."
introduction_text += f"\nI'm thinking of a number between 1 and 20."
introduction_text += f"\nIf I give you hints on whether your guesses are lower or higher."
introduction_text += f"\nThink you can guess the correct number in 6 tries?\n\n\n"

print(introduction_text)

# Strings and inputs for playing the game, quitting and instruction.
play_input_text = "So, would you like to play?\n"
instructions = "Type Y to play, or Q to quit, you can press Q at any time to quit."
play_input_text += instructions
play_status = input(play_input_text)
play_again_text = "Would you like to play again? "
quit_text = "Quitting game"


def generate_random_number():
    # generates a random number for the game between 1 and 20
    random_integer = random.randint(1, 20)
    return random_integer


def game():
    target_number = generate_random_number()
    guess_counter = 0
    while (play_status == "Y" or play_status == "y") and guess_counter <= 5:
        guess = input(f"You have {6 - guess_counter} guesses left. What is your guess ?: ")
        if guess == "Q" or guess == "q":
            print(quit_text)
            break
        elif int(guess) == target_number:
            print(f"That's right! The correct number was {target_number}!")
            print(f"{user_name}, you managed to guess the correct number in {guess_counter + 1} tries!")
            play_again = input(play_again_text + instructions)
            if play_again == "Y" or play_again == "y":
                game()
            elif play_again == "Q" or play_again == "q":
                print(quit_text)
                break
        elif guess_counter == 5:
            print(f"Ahh unlucky {user_name}, you're out of guesses. The correct number was {target_number}")
            play_again = input(play_again_text + instructions)
            if play_again == "Y":
                game()
        elif int(guess) != target_number:
            if int(guess) > target_number:
                print("That guess was too high.")
                guess_counter += 1
            else:
                print("That guess was too low.")
                guess_counter += 1


if play_status == "Y" or play_status == "y":
    game()
