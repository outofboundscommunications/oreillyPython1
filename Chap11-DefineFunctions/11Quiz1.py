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

theString = "This is now lowercase:"
answer2 = 'Parameters are placeholders in function definitions where you pass in arguments\
so the answer would thus be: "Parameters become arguments." '
answer3 = 'Yes. A function can access variables outside its body via use of the parameter. you can\
pass in the variable via a parameter and use it inside the function.'

def my_answers(num,question):
    print(60*'-')
    print('\n', 'Question#:',num)
    print(question,'\n')
    print('Answer:')

def returnAnswer1(myString):
    LString = myString.lower()
    print(myString+LString)
    
def returnAnswer2(myAnswer2):
    print(answer2)
    
def returnAnswer3(myAnswer3):
    print(answer3)
    
    
    
my_answers(1,question1)
returnAnswer1(theString)

my_answers(2,question2)
returnAnswer2(answer2)

my_answers(3,question3)
returnAnswer3(answer3)
