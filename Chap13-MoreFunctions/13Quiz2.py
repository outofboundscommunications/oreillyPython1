

question1 = 'Can a positional argument provide a value for a keyword parameter?'
question2 = 'Can a keyword argument provide a value for a positional parameter?'
question3 = 'What happens when you call a function with too many positional arguments, and the function definition doesnt have a sequence-parameter?'


def printQuestion(num,question):
    print(60*'-')
    print("Question#: %d \n" % num)
    print("%s" % question)

def printAnswer(num,answer):
    print(60*'-')
    print("Answer#: %d \n" % num)
    print("%s" % answer)

def myArguments(Arg1=1, Arg2=1):
    """function with two keywor arguments a,b and"""
    return(Arg1+Arg2)

def test_me(a, b):
    """function with two positional arguments"""
    print(a, b)

#make a call to the function to see if we can use positional arguments
#for the keyword parameters
#answer1 = myArguments(10,10)

#make a call to the function to see if we can use keyword arguments
#for the positional parameters
answer2 = test_me(a=10,b=10)

#answer3 = myArguments(10,20,30,40,50,60)

#printQuestion(1,question1)
#printAnswer(1,answer1)

printQuestion(2,question2)
printAnswer(2,answer2)

#printQuestion(3,question3)
#printAnswer(3,answer3)



