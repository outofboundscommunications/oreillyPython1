'''
Created on Dec 6, 2014

@author: jay wilner 3
'''
from xml.dom.minidom import CharacterData
print("""Question 1:
What is wrong with the following code?

print ("This is a very fun class
and I am learning about Python!")\n""")

print("""Answer 1:
it throws an error because a string in a single quote MUST begin and
end on the same line. If you replace the single quotes with three quotation marks it works fine\n""")

print("""Question 2:
What four delimiters can be used when writing string literals? 
Note: Delimiters show where strings begin and end. They are the same on both 
ends of the string.\n""")

print("""Answer 2:
1. single quote '
2. double quote "
3. triple double quote \""" 
4. triple single quote \'''
""")

print("""Question 3:
What string does the interactive Python interpreter use as a prompt?\n""")

print("""Answer 3:
the >>> string""")
