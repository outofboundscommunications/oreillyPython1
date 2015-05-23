'''
Question 1:
How do you:

check if all elements in a list, set, or tuple evaluate to true?

'''

'''
Question 2:
how do you:
return the methods and attributes associated with the value 'Python'?

'''

'''
Question 3:
how do you:
return all of the global variables?

'''

'''
Question 4:
how do you:
examine the documentation of an object?

'''

''' Answer Question 1 '''
print("Question 1:How do you: check if all elements in a list, set, or tuple evaluate to true?")
print('---------------------------------------------\n')
print('use the all() function')
myTuple = (1,4,5,77,888,'a',0)
for i,e in enumerate(myTuple):
    print(i,e)
print('for the above tuple, the all() function evaluates to: ', all(myTuple))

print('---------------------------------------------\n')

''' Answer Question 2 '''
print("Question 2:how do you: return the methods and attributes associated with the value Python?")
print('---------------------------------------------\n')
print('use the dir() function')
p = 'python'
print('the dir(python) statement evaluates to:','\n')
print(dir(p))

print('---------------------------------------------\n')


''' Answer Question 3 '''
print("Question 3:how do you: return all of the global variables?")
print('---------------------------------------------\n')
print('use the globals() function')
print('the globals() statement evaluates to:','\n')
print(globals())
print('---------------------------------------------\n')

''' Answer Question 4 '''
print("Question 4:how do you: examine the documentation of an object?")
print('---------------------------------------------\n')
print('use the help() function')
print('the help(abs) statement evaluates to:','\n')
print(help(abs))
print('---------------------------------------------\n')



