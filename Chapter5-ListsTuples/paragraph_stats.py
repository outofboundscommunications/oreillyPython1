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
charct = len(gettysburg)

lines = gettysburg.split("\n")
linect = len(lines)

wordct = 0
for line in lines:
    words = line.split()
    wordct += len(words)
    for word in words:
        lengthct[len(word)] += 1

print("The text contains", linect, "lines,", wordct, "words, and", charct, "characters.")
for i, ct in enumerate(lengthct):
    if ct:
        print("Length", i, ":", ct)