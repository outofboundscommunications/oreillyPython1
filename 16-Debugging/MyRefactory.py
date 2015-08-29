
#define list of prepositions
small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')
def book_title(title):
    """ Takes a string and returns a title-case string.
    All words EXCEPT for small words are made title case
    unless the string starts with a preposition, in which
    case the word is correctly capitalized.

    >>> book_title('DIVE Into python')
    'Dive into Python'

    >>> book_title('the great gatsby')
    'The Great Gatsby'

    >>> book_title('the WORKS OF AleXANDer dumas')
    'The Works of Alexander Dumas'
    """
    #break the title into words and convert to lower case
    lst_of_words = title.lower().split()
    #create variable to hold the new (title case) title as we build it
    new_title ='' 
    for i,word in enumerate(lst_of_words):
        #count the number of words in the title so we can use to determine if we need to add trailing space
        #if final word in title we don't want to add trailing space
        numWordsInTitle = len(lst_of_words) -1 
        #If index is 0, its the first word of the title, so just go ahead and capitalize first letter
        if i==0:
            new_title += word.title()+" "
        #check and see if the word is in the list of 'small words' or prepositions
        else:
            #if word is preposition then don't need to change case, just append word as is
            if word in small_words:
                #if it's the last word in title, don't add trailing space
                if i == numWordsInTitle:
                    new_title +=word
                else:
                    new_title +=word +" "
            #word is not a preposition so go ahead and make first letter title case.
            else:
                #if it's the last word in title, don't add trailing space
                if i == numWordsInTitle:
                    new_title +=word.title()
                else:
                    new_title +=word.title()+" "
    return new_title 

def _test():
    import doctest, MyRefactory
    return doctest.testmod(MyRefactory)

if __name__ == "__main__":
    _test()
 

'''
for title in lst_of_titles:
    print(book_title(title))
'''