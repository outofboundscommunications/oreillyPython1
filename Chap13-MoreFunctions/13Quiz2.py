
def myArguments(Arg1=1, Arg2=1):
    """function with two keyword arguments a,b and"""
    return(Arg1+Arg2)

def test_me(a, b):
    """function with two positional arguments"""
    return(a+b)

#make a call to the function to see if we can use positional arguments
#for the keyword parameters
answer1 = myArguments(10,10)

#make a call to the function to see if we can use keyword arguments
#for the positional parameters
answer2 = test_me(a=10,b=10)

print('#1',answer1)

print('#2',answer2)




