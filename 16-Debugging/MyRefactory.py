lst_of_titles =('DIVE Into python','the great gatsby','the WORKS OF AleXANDer dumas')

small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')
""" Takes a string and returns a title-case string.
All words EXCEPT for small words are made title case
unless the string starts with a preposition, in which
case the word is correctly capitalized.
"""

def book_title(title):
    print('the title passed in is: ',title)
    #break the title into words and convert to lower case
    lst_of_words = title.lower().split()
    #create variable to hold the new (title case) title as we build it
    new_title ='' 
    for i,word in enumerate(lst_of_words):
        #If index is 0, its the first word of the title, so just go ahead and capitalize first letter
        #e.g. you don't need to check if preposition or not. doesnt matter.
        if i==0:
            new_title += word.title()+" "
            #replace the existing word in the list with the new title case changed word
            #lst_of_words[i] = new_title
        #check and see if the word is in the list of 'small words' or prepositions
        else:
            #if word is preposition then skip.
            if word in small_words:
                new_title +=word+" "
                #replace the existing word in the list with the new title case changed word
                #lst_of_words[i] = new_title
            #word is not a preposition so go ahead and make first letter title case.
            else:
                new_title += word.title()+" "
                #replace the existing word in the list with the new title case changed word
                #lst_of_words[i] = new_title
    #concatenate the new, correctly cased word to the new_title trunk
    return new_title 
for title in lst_of_titles:
    print(book_title(title))

