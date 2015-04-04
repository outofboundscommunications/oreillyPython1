'''
Created on Dec 21, 2014

@author: jay wilner 3
'''


#define substring
substring = 'tacky'
#define variable to capture user input
uin = input("Please enter a string: ")
#check to see if substring contained in the uin
if substring in uin:
    print('the substring: ' + substring + ' is in the string you entered(' + uin + ')')
else:
    print('the substring: ' + substring + ' is NOT in the string you entered(' + uin + ')')


'''
#check to see if string is non-empty and contains only alphanumeric characters
if uin.isalnum():
    print('the string is non empty and contains only alphanumeric characters')
elif uin.islower():
    print('the string is lowercase')
elif uin.isupper():
    print('the string is upper')
print('hello')

'''
