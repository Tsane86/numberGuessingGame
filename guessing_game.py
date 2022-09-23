"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    # Create Random number #
    correct_answer = random.randint(1,10)
    game_continues = True
    attempts = 0
    
    # use a while loop to ask for input
    while game_continues:
        try:
            guess = int(input('Please input your guess between 1 and 10: '))
            if guess <= 0:
                raise Exception('Not a positive number, please enter a positive number!')
        except ValueError:
            print('Not a number! Please input a number next time')
        except Exception as err:
            print(err)
        else:
            if guess == correct_answer:
                print(f'Got it! It took you {attempts} attempts! Game Over!')
                game_continues = False
            elif guess < correct_answer:
                print(f'It\'s higher')
                attempts += 1
            elif guess > correct_answer:
                print('It\'s lower')
                attempts += 1


# Kick off the program by calling the start_game function.
start_game()