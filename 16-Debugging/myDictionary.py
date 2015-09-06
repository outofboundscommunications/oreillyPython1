__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
#testing out how to create a dictionary where index is integer of 
#word length and values are a list of all the words of that length,duplicates allowed

#define list of punctuation characters that we will not count
pList = ("'", ":", ",", "_", "...", "!", "-", "(", ")", ".", "?",'"',"&")

#define empty dictionary
word_dict = {}

def lenCounter(word):
    wordLength =0
    for c in word:
        if c not in pList:
            wordLength+=1  
    return wordLength

wordList = ('&','myword','word','helloword','myword','words','goodwords','word','thisword',
            'allthewords','howmanywords','finalword','mywords', 'goodwords',
           'allthewords,')

#loop through text and accumulate key, values

for word in wordList:
    #figure out length of word without punctuation
    wordLength = lenCounter(word)
    word_dict.setdefault(wordLength, []).append(word)
    
print(word_dict)
    
    
    
