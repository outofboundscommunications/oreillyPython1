'''
this is the final objective #3 in chapter 16
'''
import sys

from string import punctuation as punc 

#open the text file to read
f = open(sys.argv[1] , 'r')
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

freq = {}

#split string into words
words = text.split()

for word in words:
    wordLength = lenCounter(word)
    if wordLength in freq:
        freq[wordLength] += 1
    else:
        freq[wordLength] = 1
#for wordLength in (freq.keys()):
    #print('the word length is: ', wordLength,'and the frequency is: ',freq[wordLength])
    
#now we need to search thru the dictionary and look for all the values from high to low
#and we need to find the corresponding indexes to those values

for y in range(400, -1, -20):
    myString=""
    for wordLength in (freq.keys()):
        if wordLength==0:
            myString+='|'
        if y <=freq[wordLength]:
            myString+="**"
        else:
            myString+=" "
    print(y,myString)