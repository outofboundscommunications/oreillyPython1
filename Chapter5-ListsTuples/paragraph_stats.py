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