'''
Created on Jan 31, 2015

@author: jay wilner 3
'''
from cmd import PROMPT

'''
Objective 1:
This project tests your ability to use sets and dicts, and your ability to follow an algorithm (recipe) exactly.

1.Create a new Python source file named input_counter.py.
2.Write a program that creates an empty set and dict.
3.Write a while loop that repeatedly creates a list of words from a line of input from the user.
4.Loop through the list of words and add each one to the set. If the set increases in size (indicating this word has not been processed before), 
add the word to the dict as a key with the value being the new length of the set.
5.Using another loop, display the list of words in the dict along with their value, which represents the order in which they were discovered by the program.
6.If the user presses Enter without any text, print Finished and exit.

'''
#define empty set
myWordSet = set()
#define empty set
myDic = {}

#create a while loop that creates a list of words from the user input
while True:
  #initialize length of dict
  myDicLength = len(myDic)
  inputString = input('Enter a line of text (or Enter to quit):')
  #if user hits 'enter' then exit program/quit
  if not inputString:
      print ('Finished')
      break
  #else break up input string into individual words
  words = inputString.split()
  for word in words:
      #if the word is already in the set, just skip (continue)
      if (word in myWordSet):
          continue
      else:
          #add the word to the set
          myWordSet.add(word)
          #also add the word to the dict as a key with the value being the new length of the set
          myDicLength +=1
          myDic[word] =myDicLength

#user has hit 'enter', so we need to display the dict values
for word in (myDic.keys()):
    print(word,myDic[word])