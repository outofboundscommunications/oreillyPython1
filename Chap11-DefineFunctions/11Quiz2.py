
question1 = 'What is the prefix used for a sequence-parameter?'
question2 = 'What type of object does the sequence-parameter provide to the function body?'

answer1 = 'The prefix used is the "*" character. For example:\
def multiplier(*args):'
answer2 = 'A tuple. The interpreter collects any unmatched positional arguments into\
a tuple and then binds the tuple to the name following the asterisk in the called functions namespace.'

def printQuestion(num,question):
    print(60*'-')
    print('\n', 'Question#:',num)
    print(question,'\n')
    print('Answer:')
    
def returnAnswer(myAnswer):
    print(myAnswer)
    
    
    
printQuestion(1,question1)
returnAnswer(answer1)

printQuestion(2,question2)
returnAnswer(answer2)


