
small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')
""" Takes a string and returns a title-case string.
All words EXCEPT for small words are made title case
unless the string starts with a preposition, in which
case the word is correctly capitalized.
"""
#assign title of book
title = 'DIVE Into python'
#break the title into words and convert to lower case
print('the title we start with is: ', title)
#count the number of words in title
lst_of_words = title.lower().split()
print('the list of words we made with the split function is: ', lst_of_words)
new_title ='' 
for i,word in enumerate(lst_of_words):
    if i==0:
        #can ignore if preposition since first word, just go ahead and capitalize first letter
        print('this is the first word of the list of words:', word )
        new_title = new_title + word[0].upper()+word[1:]
        print(new_title)
        return new_title
    else:
        print('this is the :',i,'th word of the list of words: ', word)
        if word in small_words:
            new_title = new_title + word
        else:
            new_title = new_title + word[0].upper()+word[1:]

