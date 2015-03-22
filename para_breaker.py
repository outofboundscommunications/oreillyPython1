'''
Objective 1:
This project tests your ability to use more sophisticated loops.

Create a new Python source file named para_breaker.py.
Write a program to break up a paragraph into sentences and phrases. 
Sentences are delineated by periods
Phrases are delineated by commas.
Print the results to the screen. 
You will need to use a loop within a loop.
Use the text from the second paragraph of the United States Declaration of Independence (provided below).
'''

#assign the text to a string variable
paragraph='''
Four score and seven years ago, our fathers set for a nation. Delivered under God, for ever ours only, to be managed by the people.
'''
#set sentence counter to zero
numSentences = 0

while True:
    for c in paragraph:
        #set position counter to zero
        pos = 0
        ######  Loop through string until you find period, that is first sentence ########
        #if the character is a period, you have found a sentence
        if c == ".":
            #increment the sentence counter by one
            numSentences +=1
            #print out row of stars as top border
            print('***********************************')
            #print sentence number
            print("Sentence #:",numSentences)
            #chop off that sentence and save so you can look for phrases
            mySentence = paragraph[:pos]
            print('the sentence is: ',mySentence)
            #set phrase counter to zero
            numPhrases = 0
            ###### loop through sentence until you find a comma, that is the first phrase #########
            for character in mySentence:
                #set position counter to zero
                myPosition = 0
                #look for a comma which denotes a phrase
                if character ==",":
                    #increment the phrase counter by one
                    numPhrases +=1
                    #print phrase number and the phrase
                    print("Phrase #: ",numPhrases,mySentence[:myPos])
                    #reset the string from (current position +1) forward 
                    mySentence = mySentence[myPosition+1:]
                    break
                #else the character isnt a comma so increment the counter by one
                myPosition +=1
            else:
                print('mySentence')
        #else the character isnt a period so increment the position counter by one
        pos += 1
    else:
        print(paragraph)
        print('hello')
        break
    