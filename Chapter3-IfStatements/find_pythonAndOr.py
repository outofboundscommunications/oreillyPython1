'''
Created on Dec 20, 2014

@author: jay wilner 3
'''
#program to check various conditions that are combined
s = 'ABC'
t = 'BBC'

if s.isupper() and s.startswith("A"):
    print("s is upper case starting with A")
elif t.isupper() and s.startswith("A"):
    print("t is upper case starting with A")
elif 1 !=2:
     print('does not compute')   

    