'''
Created on Dec 26, 2014

@author: jay wilner 3
'''

#!/usr/local/bin/python3
"""Program to locate the first space in the input string."""
s = input("Please enter a string: ")
pos = 0
for c in s:
    if c == " ":
        print("First space occurred at position", pos)
        break
    pos += 1
else:
    print('no spaces in that string')
