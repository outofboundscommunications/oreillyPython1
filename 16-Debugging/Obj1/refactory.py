
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
    print('the title we started with is: ', title)
    lst_of_words = title.lower().split()
    print('the list of words we made with the split function is: ', lst_of_words)
    #count the number of words in title
    num_of_words = len(lst_of_words)
    #if no words, skip
    if num_of_words < 1:
        return ''
    #retrieve the first word in the lst_of_words
    new_title = lst_of_words.pop(0)
    print('the first word of the title is found using the pop[0] method and is', new_title)
    #convert the first character of first word to upper case and concatenate to remainder
    new_title = new_title[0].upper() + new_title[1:]
    print('the new stub of the title is: ', new_title)
    #tpl_of_words = tuple(lst_of_words)
    #for word in tpl_of_words:
    for word in lst_of_words:
        print('now we are looping thru the words in the lst_of_words. we are at: ', word)
        prep_word = False
        #loop thru all words in preposition list
        for prep in small_words:
            print('Now, for ', word, ' we loop thru all the words in preposition list and see if ', word, 'is on the list. we are at: ',prep)
            if prep == word:
                print('found a prep word. it is:' , word)
                new_title = new_title + ' '
                print('the new title + space is: ',new_title)
                new_title = new_title + word
                print('the new title + prep word is: ',new_title)
                #prep_word = True
                #break
                continue
        #if prep_word == True:
            #print('now we are going to continue')
            #continue
        print('we did not find any matches. the word was not on the preposition list. so now we are in the outer new title loop')
        new_title = new_title + ' '
        new_title = new_title + word[0].upper()
        new_title = new_title + word[1:]
    return new_title

def _test():
    import doctest, refactory
    return doctest.testmod(refactory)

if __name__ == "__main__":
    #_test()


    