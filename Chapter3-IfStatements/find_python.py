'''
Created on Dec 20, 2014

@author: jay wilner 3
'''
"""Detect any mention of Python in the user's input."""
uin = input("Please enter a sentence: ")
'''
if "python" in uin.lower():
    print("You mentioned Python.")
elif "php" in uin.lower():
    print("you mentioned php")
else:
    print('didnt see python there.')
'''    

if "python" in uin:
    print("You mentioned Python.")
elif "python" in uin.upper():
    print("you mentioned python and it was lower case")
else:
    print('didnt see python there.')