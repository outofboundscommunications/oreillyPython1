
question1 = 'Write a function that returns the string "This is now lowercase:" plus the \
lowercase representation of its string argument, as a single string.'
question2 = 'Do parameters become arguments or do arguments become parameters?'
question3 = 'Can a function access variables defined outside of its body? If so, where?'

answer2 = 'Parameters are placeholders in function definitions where you pass in arguments\
so the answer would thus be: "Parameters become arguments." '
answer3 = 'By default, we can get the contents of a global variable inside the body of a function. \
But if we want to change a global variable in a function, we must use the global keyword within the function.'

globalVariable = 200

#function that prints out each question to the screen

def printQuestion(num,question):
    print(60*'-')
    print('\n', 'Question#:',num)
    print(question,'\n')
    print('Answer:')

###Answer 1 stuff ###    

printQuestion(1,question1)

def returnAnswer(myString):
    text = "This is now lowercase:"
    LString = myString.lower()
    text+=LString
    return text

v = returnAnswer('hello There How Are You Today?')
print(v)

##Answer 2 stuff ###
def returnAnswer2(myAnswer2):
    print(answer2)

printQuestion(2,question2)
returnAnswer2(answer2)

###Answer 3 stuff ###
def returnAnswer3(myAnswer3):
    global globalVariable
    print(globalVariable)
    globalVariable+=100
    print(globalVariable)
    
printQuestion(3,question3)
returnAnswer3(answer3)


