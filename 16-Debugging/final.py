__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
'''
#Objective 2:
This project tests your basic ability to build a complex program from the relatively limited amounts of Python you already know.

Create a new Python source file named final.py.
Write a program that meets the following specifications:
1. Call the program with an argument, it should treat the argument as a filename, and process the content of the file.
2. The program reads all the input, splitting it up into words, and computes the length of each word. Punctuation marks should not 
be included as a part of the word, so "it's" should be counted as a three-character word, and "final." should be counted as a 
five-character word.
3. The example text includes a "word" of zero length (the "&"); your solution should handle this.
4. When all input has been processed, the program should print a table showing the word count for each of the word lengths 
encountered. Your mentor will run your code against several standardized inputs to verify the correctness of your logic.


Below is an example of output from running the program using the text in this file as input. (The text is the United States 
Declaration of Independence). Copy the text in this file. Create a new file and paste the copied text into it, and save it 
as declaration.txt in the same folder where your final.py program is located.

Here is some sample output.

 Length Count
 1 16
 2 267
 3 267
 4 169
 5 140
 6 112
 7 99
 8 68
 9 61
 10 56
 11 35
 12 13
 13 9
 14 7
 15 2
Also, you will probably want to define a function to return the length of each word, since the built-in len() function will 
include punctuation characters.

'''

'''
Created on Jan 1, 2015

@author: jay wilner 3
'''
"""Count the words, lines and characters in a chunk of text."""

gettysburg = """\
Four score and seven years ago our
fathers brought forth on this continent,
a new nation, conceived in Liberty, and
dedicated to the proposition that
all men are created equal.
furniture store hinesville ga
furniture stores in hinesville ga
gibson furniture
mattress hinesville ga
a a b c d

"""

lengthct = [0]*20 # a list of 20 zeroes
print(lengthct)
#counts characters in text
charct = len(gettysburg)

lines = gettysburg.split("\n")
#counts lines in text
linect = len(lines)

wordct = 0
for line in lines:
    #split each line into words
    words = line.split()
    #count the number of words in the line
    wordct += len(words)
    for word in words:
        #increment the counter for the word of length, len(word), by 1
        lengthct[len(word)] += 1

print("The text contains", linect, "lines,", wordct, "words, and", charct, "characters.")
for i, ct in enumerate(lengthct):
    if ct:
        print("Length", i, ":", ct)