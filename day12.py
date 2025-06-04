import random


game = True
difficulty = None
correct_number = None

def new_game():
    global game, difficulty, correct_number
    attempts = 10
    difficulty = input("I'm thinking of a number between 1 and 100.Choose a difficulty. type 'easy' or 'hard': ")
    correct_number = random.randint(3, 9)
    print("Random number is: ", correct_number)
    game = True

new_game()

while game == True:
    attempts = 10
    if difficulty == "easy":
            while attempts > 0:
                guess = int(input("Write your guessed number: "))
                if guess == correct_number:
                    print("Congratulations! You guessed the number!")
                    play_again = input("Play again? Type 'y' or 'n': ")
                    if play_again.lower() == 'y':

                        new_game()
                    else:
                        game = False
                        break

                if guess < correct_number:
                    print("too low, try again")
                    print(f"You have {attempts - 1} attempts left.")
                    attempts = attempts - 1

                else:
                    print("too high, try again")
                    print(f"You have {attempts - 1} attempts left.")
                    attempts = attempts - 1

            print("Here")
    elif difficulty == "hard":
            attempts = 5
            print(f"You have {attempts} attempts to guess the number.")

    else:
            print("Invalid difficulty level. Please type 'easy' or 'hard'.")
            exit()
