'''
Objective 1:
This project tests your ability to use sequences.

1.Create a new Python source file named word_list.py.
2.Make the program read a string from the user and create a list of words from the input.
3.Create two lists, one containing the words that contain at least one upper-case letter and one of the words that don't contain any upper-case letters.
4.Use a single for loop to print out the words with upper-case letters in them, followed by the words with no upper-case letters in them, one word per line.
5.Verify that your program works correctly, and hand it in.
'''

#define list for upper case words
upperCaseList=[]
#define list for lower case words
lowerCaseList=[]

#capture user input
s = input("Enter your string: ")
#strip raw input string of any spaces, tabs and then split into individual words
words = s.strip().split()
#print(words)
#loop thru each of the words in the string and place word in correct CaseList
for word in words:
    #loop thru each character in the word to check for any upper case characters
    for c in word:
         #if character is uppercase, then add its 'parent' word to the upperCaseList
        if c.isupper():
            upperCaseList.append(word)
            break
    #no characters in the word are uppercase so word is lowerCase
    else:
        lowerCaseList.append(word)
for listWord in upperCaseList:
    print(listWord)

for listWord in lowerCaseList:
    print(listWord)

