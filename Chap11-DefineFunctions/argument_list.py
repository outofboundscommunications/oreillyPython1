"""
demonstrates the use of multiple positional parameters when you don't know how many are going \
to be called. so you use a special syntax: *name in the function definition

When you prefix the positional parameter with the asterisk (*) character in the function definition, this tells the \
interpreter to collect any unmatched positional arguments into a tuple and then bind the tuple to the name following \
the asterisk in the called function's namespace. 
"""
def multiplier(*args):
    """ Multiply the arguments together and return the result.
        Return 0 if nothing is provided.
    """
    if not args:
        return 0
    product = args[0]
    for a in args[1:]:
        print('a is: ',a)
        product *= a
    return product,args

print(multiplier())
print(multiplier(1,2,3,4))
print(multiplier(6,7,8,9,10,11,12,13))
print(multiplier(10,20,100))