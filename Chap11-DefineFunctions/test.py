__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
#


def returnAnswer(myString):
    text = "This is now lowercase:"
    LString = myString.lower()
    text+=LString
    return text

v = returnAnswer('hello There How Are You Today?')
print(v)