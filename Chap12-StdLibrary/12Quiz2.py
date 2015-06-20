'''
Question 1:
What is sys.path? How is it used by the Python interpreter?

'''

'''
Question 2:
What value does a module's __name__ attribute receive if the module is run as a program?
'''

'''
Question 3:
What is wrong with from module import *?
'''

question1 = 'What is sys.path? How is it used by the Python interpreter?'
question2 = 'What value does a modules __name__ attribute receive if the module is run as a program?'
question3 = 'What is wrong with from module import *?'

answer1 = 'sys.path is a list of strings that specifies the search path for modules. \
Example paths include:\
usr/local/python34/lib/python34.zip \
usr/local/python34/lib/python3.4 \
usr/local/python34/lib/python3.4/plat-linux \
usr/local/python34/lib/python3.4/lib-dynload \
usr/local/python34/lib/python3.4/site-packages \
'


answer2 = 'When a module runs as a program, __name__ receives a special value __main__'

answer3 = 'it puts the imported module in charge of what gets loaded into your namespace.\
if you are not careful, it can get confusing understanding the names of your local modules \
in light of any duplicate imported modules. If your local modules had the same name, the imported\
module will then be in control.'

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

printQuestion(3,question3)
returnAnswer(answer3)



