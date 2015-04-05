'''
Created on Feb 28, 2015

@author: jay wilner 3
'''
"""Validate user input"""

while True:
    s = input("Type 'yes' or 'no':")
    if s == 'yes':
        break
    if s == 'no':
        break        
    print("Wrong! Try again.")
print(s)