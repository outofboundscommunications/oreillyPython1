import sys

from string import punctuation as punc 

#define list of punctuation characters that we will not count
#pList = ("'", ":", ",", "_", "...", "!", "-", "(", ")", ".", "?",'"',"&")

#define empty dictionary
word_dict = {}

#initialize the list that counts frequency of word length
lengthct = [0]*20 # a list of 20 zeroes

#open the text file to read
f = open(sys.argv[1] , 'r')
text = f.read()
#split string into words
words = text.split()

#function that creates a one to many dictionary of word length and words of that length
def wordDict(word):
    for word in words:
        #figure out length of word without punctuation
        wordLength = lenCounter(word)
        word_dict.setdefault(wordLength, []).append(word)
        
#function that counts length of a word but skips punctuation
def lenCounter(word):
    wordLength =0
    for c in word:
        if c not in punc:
            wordLength+=1  
    return wordLength

#process the words
for word in words:
    #call function to calculate word length, then increment the counter for the word of that length
    #don't count words of zero length (e.g. '&')
    if lenCounter(word)>0:
        lengthct[lenCounter(word)] += 1
    #append length of word and word value as key,value pairs in dictionary
    wordLength = lenCounter(word)
    word_dict.setdefault(wordLength, []).append(word)

for i, ct in enumerate(lengthct):
    if ct:
        print("Length", i, ":", ct)     

