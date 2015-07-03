'''
Question 1:
What is the dict-parameter?
What type of object is provided by the dict-parameter?

'''

question1 = 'What is the dict-parameter? What type of object is provided by the dict-parameter?'


answer1 = 'We know that when an unknown number of positional arguments will be provided, \
we can capture the extra ones (that dont correspond to any of the formal parameters) \
by specifying a parameter name that is preceded by a single asterisk (*). \
In much the same way, you can capture keyword arguments whose names do not correspond to the name \
of any parameter. To do that, we prefix the last defined parameter with two asterisks, \
and call a dict-parameter.The interpreter matches up the positional and keyword arguments with their \
corresponding parameters, then takes any unmatched keyword arguments and puts them into a dict, \
which it binds to the dict-parameter.'

def printQuestion(num,question):
    print(60*'-')
    print('\n', 'Question#:',num)
    print(question,'\n')

printQuestion(1,question1)

print("Answer: \n %s" % answer1)





