
""" Demonstrates capture of keyword arguments and also positional arguments

var: positional argument
*args: arbitrary positional arguments
**kwargs: arbitrary keyword arguments

"""

def keywords(**kwargs):
    "Prints the keys and arguments passed through"
    for key in kwargs:
        print("Key: {0}: Value: {1} ".format(key, kwargs[key]))

def keywords_as_dict(var,**kwargs):
    "Returns the keyword arguments as a dict"    
    return var,kwargs

def argPositional(*args):
    "Prints the positional arguments passed through"
    for a in args:
        print("{0}".format(a))

def keywords_as_dictEnum(**kwargs):
    "Returns the keyword arguments as a dict but using an enumerator"    
    print("the number of elements in the dict is: ", len(kwargs))
    for k in kwargs.items():
        print(k)
        
if __name__ == "__main__":
    print("*"*80)
    print("example #1 - calling function 'keywords(**kwargs)':")
    keywords(guido="Founder of Python", python="Used by NASA and Google")
    print("*"*80)
    
    print("example #2 - calling function 'keywords_as_dict(var,**kwargs)':")
    print(keywords_as_dict('my var',guido="Founder of Python", python="Used by NASA and Google"))
    print("*"*80)
    
    print("example #3 - calling function 'argPositional(*args)':")
    argPositional('hello there',"Founder of Python", "Used by NASA and Google")
    print("*"*80)
    
    print("example #4 - calling function 'keywords_as_dictEnum(**kwargs)':")
    keywords_as_dictEnum(guido="Founder of Python", python="Used by NASA and Google")
    print("*"*80)