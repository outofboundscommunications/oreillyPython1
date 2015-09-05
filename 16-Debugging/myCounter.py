__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
#my custom word length counter that excludes punctuation

#define list of punctuation characters that we will not count
pList = ("'", ":", ",", "_", "...", "!", "-", "(", ")", ".", "?",'"')

wordList = ("'myword",':word',',_helloword','...theword','!word','-word','(word',')word','.word','?word','"word')

def lenCounter(word):
    wordLength =0
    for c in word:
        if c not in pList:
            wordLength+=1  
    return wordLength

for myWord in wordList:
    print('the length of: ',myWord, ' is: ')
    print(lenCounter(myWord))