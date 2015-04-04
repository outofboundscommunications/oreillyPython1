'''
Created on Dec 20, 2014

@author: jay wilner 3

Objective 1:
This project tests your ability to use conditional tests and write code that responds differently to different inputs.

Create a new Python source file named check_string.py.
Write a program that asks the user to input a string. 
Verify with tests that the string is all in upper case and ends with a period. 
If either of these tests fails, print an appropriate message. If both tests succeed, print a message that indicates the string is acceptable.
Verify that your program works correctly and hand it in.
Here are examples of how the program might appear when run twice:

Please enter an upper-case string ending with a period: lower case input
Input is not all upper case.
Input does not end with a period.
Please enter an upper-case string ending with a period: THIS IS OK.
Input meets both requirements.
'''
#define variable to capture user input
uin = input("Please enter a sentence: ")
#String is all upper case
if uin.upper() == uin:
    #string contains period
    if uin.endswith("."):
        print('the input was all upper case AND there was a period. Input acceptable!')
    #string does not contain period
    else:
        print('the input as all upper case BUT there was not a period.\n' 'Please enter an upper-case string ending with a period.')
#string is not upper case
#string contains period
elif uin.endswith('.'):
    print('the input was not upper case BUT there was a period. Input not acceptable.\n' 'Please enter an upper-case string ending with a period.')
#string does not contain period
else:
    print('the input was not upper case AND there was not a period. Input not acceptable.\n' 'Please enter an upper-case string ending with a period.')
    

