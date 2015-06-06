'''
Question 1:
Write a function that returns the string "This is now lowercase:" plus the 
lowercase representation of its string argument, as a single string.

'''

'''
Question 2:
Do parameters become arguments or do arguments become parameters?

'''

'''
Question 3:
Can a function access variables defined outside of its body? If so, where?

'''

question1 = 'Write a function that returns the string "This is now lowercase:" plus the lowercase representation of its string argument, as a single string.'
question2 = 'Do parameters become arguments or do arguments become parameters?'
question3 = 'Can a function access variables defined outside of its body? If so, where?'

theString = "This is now lowercase."
answer2 = 'Parameters are placeholders in function definitions where you pass in arguments\
so the answer would thus be: "Parameters become arguments." '
answer3 = 'By default, we can get the contents of a global variable inside the body of a function. \
But if we want to change a global variable in a function, we must use the global keyword within the function.'

globalVariable = 200

def printQuestion(num,question):
    print(60*'-')
    print('\n', 'Question#:',num)
    print(question,'\n')
    print('Answer:')

def returnAnswer1(theString):
    #define the list to contain the two strings
    text = ''
    LString = theString.lower()
    text+=theString
    text+=LString
    return(text)

printQuestion(1,question1)
print(returnAnswer1(theString))


def returnAnswer2(myAnswer2):
    print(answer2)

printQuestion(2,question2)
returnAnswer2(answer2)

def returnAnswer3(myAnswer3):
    global globalVariable
    print(globalVariable)
    globalVariable+=100
    print(globalVariable)
    
printQuestion(3,question3)
returnAnswer3(answer3)


