'''
Created on Feb 28, 2015

@author: jay wilner 3
'''
"""Validate user input"""
  
valid_inputs = ['yes', 'no', 'maybe']
input_query_string = 'Type %s: ' % ' or '.join(valid_inputs)
while True:
    s = input(input_query_string)
    if s in valid_inputs:
        break
    print("Wrong! Try again.")
print(s)