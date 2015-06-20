'''
Question 1:
Write code that:

imports the time module from the Python standard library.
imports the sys library, giving it the name "system."
imports your own module called actions.py.

'''

'''
Question 2:
If actions.py contains a function named "jump," how would you import just that function?
How would you import just that function and bind it to the name "leap"?
'''

question1 = 'Write code that: \
imports the time module from the Python standard library. \
imports the sys library, giving it the name "system." \
imports your own module called actions.py. \
'
question2 = 'If actions.py contains a function named "jump," how would you import just that function? \
How would you import just that function and bind it to the name "leap"?'

#answer 1:

import time
import sys as system
import actions

#answer 2:
from actions import jump
from actions import jump as leap

def printQuestion(num,question):
    print(60*'-')
    print('\n', 'Question#:',num)
    print(question,'\n')
    print('Answer:')

printQuestion(1,question1)

printQuestion(2,question2)



