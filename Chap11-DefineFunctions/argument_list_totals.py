
"""
Sometimes when you create a Python function, you don't know how many arguments you are going to get and you
want the caller to be able to provide any number of arguments. For example, you may want to create a function that
takes all the numbers given as parameters and multiply them together. To do this, we use a special parameter
specification, *name -- called a sequence paramter. There can be only one such parameter, and it must follow any \
standard positional and/or keyword parameters.

When you prefix the parameter with the asterisk (*) character in the function definition, this tells the interpreter to collect
any unmatched positional arguments into a tuple and then bind the tuple to the name following the asterisk in the
called function's namespace. 

The * sequence parameter must follow any standard positional or keyword parameters. 

This can be useful when regular arguments are also required. For instance, you may want to provide an optional \
amount to be added to the product. You'd accomplish that by using a keyword argument with a default value of zero. 

"""
def multiplier(total=0.0, *args):
    """ Multiply the arguments together, add a prior total, and return the result.
    Return 0 if nothing is provided.
    """
    if not args:
        return total
    product = args[0]
    for a in args[1:]:
        product *= a
    print('the total sales are: ', '$ %.2f' % (total), 'the arguments are: ',args)
    print("the multiplier product sales of all the arguments is:", "{0:.2f}".format(product))
    #add the product to the total
    return product + total


if __name__ == "__main__":
    (multiplier(1,2,3,4))
    (multiplier(6,7,8,9,10,11,12,13))
    (multiplier(10,20,100))