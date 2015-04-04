'''
Question #1:
How do you display braces '{ }' in your formatted output?

Consider the expression below (incomplete): 

>>> thestring.format("Hello") # just "Hello" passed in
'{Hello} world' 

What would thestring need to be? If the input were "Other" then the output would be "{Other} world" i.e. real substitution is happening 

'''
    
''' Answer Question 1 '''


print("{{{}}}".format("hello"))

'''teacher's add'l question 1:

Consider the expression below (incomplete): 

>>> thestring.format("Hello") # just "Hello" passed in
'{Hello} world' 

What would thestring need to be? If the input were "Other" then the output would be "{Other} world" i.e. real substitution is happening 

'''

print("{{a}}".format(a="hello"))


