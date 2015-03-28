'''---------------------------------
Question 1:
When a sequence of conditions is evaluated using if ... elif... elif ... is the else keyword mandatory?
------------------------------------'''
#Answer 1: 

#program to check various conditions and see if the 'else' keyword is needed
s = 'ABC'
t = 'BBC'

if s.isupper() and s.startswith("A"):
    print("s is upper case starting with A")
elif t.isupper() and s.startswith("A"):
    print("t is upper case starting with A")
elif 1 !=2:
    print('does not compute')   

''' ---------------------------------
Question 2:
Write an expression that will be True if the last three characters in s are "end".
'''

''' 
Answer 2:
'''
'''
#define variable to capture user input for primary string we search within for substring
s = input("Please enter a string for question 2: ")

#define substring we are looking for
substring = 'end'

#check to see if string is non-empty and contains only alphanumeric characters
if s.endswith(substring):
    print('the string: ' + s + ' contains the substring:' + substring)
else:
    print('the string: ' + s + ' does NOT contain the substring:' + substring)

-----------------------------------'''

''' -------------------------------
Question 3:
What keyword can you put between two conditions so that the result of the overall expression is true only when both conditions are true?
'''
'''
#define variable to capture user input for primary string we search within for substring
s = input("Please enter a string for question 3: ")

#define substring we are looking for
substring = 'end'

#create a set of two conditions joined with an 'AND' so we can test our answer
#check to see if: 
# (1) primary string ends with substring AND 
# (2) primary string is lower case
if s.endswith(substring) and s.lower()==s:
    print('the string- ' + s + ' - ends with the substring:' + substring)
    print('and the string- ' + s + ' - is lower case. Thus, our "AND" keyword worked to join these two conditions together')
else:
    print('the string didnt meet our conditions')

'''