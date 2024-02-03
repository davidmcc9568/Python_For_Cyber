'''
ASSIGHNMENT INSTRUCTIONS:

Using what we know so far do the following:
Have a variable with a number between 1 and 20 for the user to guess. (you can research random package if you are feeling frisky).
Using a loop, ask your user for a number between 1 and 20 (with exception handling in case they enter a string).
Check user input against the number you have stored.
When they get it correctly show a success message and end the program.

BONUS

If you are feeling extra confident:
Track how many times the user has guessed.
Limit the number of guesses and end the program after the user has guessed too many times.
Display how many guesses the user took to get the correct answer.
'''
'''
My focus in this assighnment was error handling. I utalized a try/except statment and nested if/else statements to accomplish this. 
'''
import random as r # import the random module to generate a random number

play = True # set boolean value for while loop

while play == True:
    start = input('Would you like to play a guessing game? y/n ')

    if start not in ('y', 'n', 'Y', 'N'):
        print('Please enter y or n')
    elif start in ('y', 'Y'):
        num = r.randrange(1, 21) # set a random number between 1 and 20

        try: # try/except statement for error handling
            count = 1 # counter to keep track of number of attempts. set to 1 instead of 0
            while count <= 3: # set max count as 3 to give user three guesses (1, 2, and 3)
                guess=int(input('Guess a number between 1 and 20>> ')) # converted user input to int

                if guess > num: # if the user's guess is greater than the number, give feedback to user and add 1 to the count
                    print('Sorry, your guess was too high try again')
                    count+=1

                elif guess < num: # if the user's guess is less than the number, give feedback to user and add 1 to the count
                    print('Sorry, your guess was too low, try again')
                    count+=1

                elif guess == num: # if the user guessed correctly, they are congratulated and the program ends
                    print('Congrats!! You guessed the number!')
                    print(f'Number of guesses: {count}') # tells the user how many guesses they used to get the correct number
                    break # ensures the program ends if the user guesses correctly

            else: # if user runs out of guesses, feedback is given and the program ends
                print('You have run out of guesses. Better luck next time.')

        except ValueError as e: # specified ValueError 
            print(f'Caught an error: {e}. Input an integer as a guess to solve this error.')
            continue # loops back through program to ask the user to if they want to play again

    elif start == 'n' or 'N': 
        sure = input('Are you sure? y/n ') # if user decides they don't want to play, give them another chance to play before ending the game

        if sure not in ('y', 'n', 'Y', 'N'):
            print('Please enter y or n')

        elif sure in ('y', 'Y'):
            print('Thank you for playing')
            play = False # set play varibale to false to end the program

        elif sure in ('n', 'N'):
            print('Time for another round ')
            continue # program goes back through the loop again if the user wants to keep playing