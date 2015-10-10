'''
need to figure out how to work with a dictionary to find the min and max
of the index and the min and max of the values

in this case, the index is the word length and the values are the count of words of that length

'''
import sys

from string import punctuation as punc 

#open the text file to read
f = open('testfile.txt', 'r')
text = f.read()
#split string into words
words = text.split()

#function that counts length of a word but skips punctuation
def lenCounter(word):
    wordLength =0
    for c in word:
        if c not in punc:
            wordLength+=1  
    return wordLength

#define dictionary that will hold word length (key) and frequency (value)
freq = {}

#split input file of text into words
words = text.split()

#process each word 
for word in words:
    wordLength = lenCounter(word)
    if wordLength in freq:
        freq[wordLength] += 1
    else:
        freq[wordLength] = 1
for wordLength in (freq.keys()):
    print('the word length is: ', wordLength,'and the frequency is: ',freq[wordLength])

for k, v in freq.items():
    print(k, v)

print('the keys in the dict are: ', freq.keys())

for k in freq.keys():
    print(k)

#figure out lowest value of the index

xMin = min(freq)
print('the minimum in the indexes is (x min): ', xMin)
xMax = max(freq)
print('the max in the indexes is (x max): ', xMax)

#figure lowest value in y axis

#yMin = min(freq[wordLength]
yMin = min(freq.values())
print('the minimum of the frequency counts is (y min) : ', yMin)

yMax = max(freq.values())
print('the max of the frequency counts is  (y max): ', yMax)
