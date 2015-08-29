""" Takes a string and returns a title-case string.
All words EXCEPT for small words are made title case
unless the string starts with a preposition, in which
case the word is correctly capitalized.
"""
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

def _test():
    import doctest, MyRefactory
    return doctest.testmod(MyRefactory)
    print('test successful')
    
if __name__ == "__main__":
    _test()

