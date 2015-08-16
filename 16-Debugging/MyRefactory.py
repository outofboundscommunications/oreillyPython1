
small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')
""" Takes a string and returns a title-case string.
All words EXCEPT for small words are made title case
unless the string starts with a preposition, in which
case the word is correctly capitalized.
"""
#assign title of book
title = 'DIVE Into python'
#break the title into words and convert to lower case
print('the title we started with is: ', title)
#count the number of words in title
lst_of_words = title.lower().split()
print('the list of words we made with the split function is: ', lst_of_words)
'''
for word in lst_of_words:
        print('now we are looping thru the words in the lst_of_words. we are at: ', word)
        #count the number of words in title
        num_of_words = len(lst_of_words)
        #initialize counter
        wordCounter = 0
        #check to see if the word is the first word in the lst_of_words. if it is, we don't need to check if preposition or not
        if word
        #check to see if the word is in the preposition list
        if word in small_words:
            print('the word,',word, ' is a preposition.')
        else:
             print('the word,',word, ' is not a preposition.')
'''
for i,word in enumerate(lst_of_words):
    if i==0:
        print('this is the first word of the list of words:', word )
        new_title = new_title + word[0].upper()
    else:
        print('this is the :',i,'th word of the list of words: ', word)
