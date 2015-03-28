'''
Created on Dec 20, 2014

@author: jay wilner 3

Objective 1:
This project tests your ability to use for and while loops.

Create a new Python source file named guess.py.
Write a program that uses a while loop to ask the user to guess a number. 
Each guess should be checked against a number stored in the "secret" variable, to which a value between 1 and 20 should be assigned at the start. 
Otherwise it should report whether the guess was higher or lower than the secret. 
If the user guesses correctly, the loop should terminate. 
The loop should also keep a count of the user's guesses, and should terminate if the user makes five incorrect guesses. 
After the loop is over, the program should print the secret if the user didn't guess it, or a congratulatory message if the user guessed correctly.
Verify that your program works correctly, both when the user guesses correctly and when they make five incorrect guesses.
'''

#define secret number user has to guess
secretVariable = 13
#define max number of guesses
maxGuesses = 5
#initialize counter for guesses
numGuesses =0

while numGuesses < 5:
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

