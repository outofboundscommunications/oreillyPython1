"""
Objective 1:
This project further tests your ability to write and use custom functions.

Create a new Python source file named caser.py.

Create these functions:
capitalize accepts a string parameter and applies the capitalize() method.
title accepts a string parameter and applies the title() method.
upper accepts a string parameter and applies the upper() method.
lower accepts a string parameter and applies the lower() method.
exit ends the program.

Store these functions in a dict with the keys matching the function names.

Create a while loop that requests two inputs from the user: one of the above function names, and any string.

Use function dispatch to get the correct function based on the first input, and then apply that function 
to the second input.


"""

def capitalize(text):
    """capitalize everything"""
    print(text.capitalize())
    
def title(text):
    """adds title case to everything."""
    print(text.title())
    
def upper(text):
    """applies upper case to everything """
    print(text.upper())
    
def lower(text):
    """applies lower case to everything"""
    print(text.lower())
    
def exit(text):
    """exits the program """
    print('goodby for now...')
    sys.exit()
    
    
if __name__ == "__main__":
    switch = {
        'capitalize': capitalize,
        'title': title,
        'upper': upper,
        'lower': lower,
        'exit' : exit
    }

    options = switch.keys()
    prompt = 'Pick an option from the list ({0}): '.format(', '.join(options)) 
    myText = 'Give some text: '
    while True:
        #prompt for selection
        inp = input(prompt)
        #get the value for the input key
        option = switch.get(inp, None)
        if option:
            #prompt for text phrase
            myText = input(myText)
            option(myText)
        else:
            print('Please select a valid option!') 