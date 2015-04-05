__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
#
##!/usr/local/bin/python3
"""Count the number of different words in a text."""

text = """\
military credit furniture
military furniture financing
military furniture
military financing electronics

"""

for punc in ",?;.":
    text = text.replace(punc, "")
print(text)
words = set(text.lower().split())
print("There are", len(words), "distinct words in the text.")
for word in words:
    print (word)
