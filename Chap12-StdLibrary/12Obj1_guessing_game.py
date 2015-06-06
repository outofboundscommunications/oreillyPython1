'''
Objective 1:
This project tests your ability to use modules and imports.

1. Create a new Python source file named guessing_game.py.
2. Import the random module.
3. Use the help() function on the random module to determine how to generate a random number 
between 1 and 99 inclusive.
4. Generate a random number between 1 and 99 and store it in a variable.
Use a while loop to accept integers from the user (don't forget—you'll need to convert the input string).
Compare the user's guess with the saved random number.
If the user successfully guesses the target number, inform them and terminate the program.
Otherwise, inform the user whether their guess was higher or lower than the saved random number and 
loop around to allow them to guess again.
Below is an example of possible output from running the program.

Guess a number: 25
Too low
Guess a number: 75
Too high
Guess a number: 60
Too high
Guess a number: 45
Too low
Guess a number: 53
You guessed it!

'''

import random

randomNumber = random.randint(1,99)

#define secret number user has to guess
secretVariable = randomNumber
#define max number of guesses
maxGuesses = 50
#initialize counter for guesses
numGuesses =0

while numGuesses < maxGuesses:
     #get user input for number guess
     s = int(input("Guess a number: "))
     #check to see if they guessed correctly
     if s == secretVariable:
        #increment the counter by one
        numGuesses +=1
        #print out their success
        print('you got it right after only: ' + str(numGuesses) + ' guess(es)!')
        #game over, exit
        break
     else:
        #they didnt guess correctly so figure out if their guess was too high or too low
        if s < secretVariable:
            print('guess higher')
        else:
            print('guess lower')
        #increment counter by one
        numGuesses +=1
        print('that makes: ' + str(numGuesses) + ' guess')
else:
    print('looks like you ran out of guesses. game over')    
