'''
this is the final objective #3 in chapter 16
------------------------------------------------------------------

 Length    Count
       1       16
       2      267
       3      267
       4      169
       5      140
       6      112
       7       99
       8       68
       9       61
      10       56
      11       35
      12       13
      13        9
      14        7
      15        2

  400 -|                                             
       |                                             
       |                                             
       |                                             
       |                                             
  300 -|                                             
       |                                             
       |   ******                                    
       |   ******                                    
       |   ******                                    
  200 -|   ******                                    
       |   ******                                    
       |   *********                                 
       |   ************                              
       |   ************                              
  100 -|   ***************                           
       |   ******************                        
       |   ************************                  
       |   ***************************               
       |   ******************************            
    0 -+-+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-
       | 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16

----------------------------------------------------------------------
notes from teacher:

The appended test file contains only 2- and 8-letter words.  The algorithm should be generic enough to graph it properly,
with two vertical bars, one over 2, the other over 8.  Remember to test all word lengths between min and max values,
even those *not in the dict* because those need "  " instead of "**" just as much.

Remember your "{}".format() tricks for right justify and fixed width.  Your y-axis needs to not be jaggedy / raggedy just because
some labels / numbers have more digits.

Good work so far.


-Kirby

--------------------------------------------------------------------

notes from kirby, second attempt:

I'd say this is done but for the final line of x-axis values.  Most conventions around histograms
were established by the histogram-using community long before Python or computer programming.
Graphs tend to use round numbers for labels.  Writing a truly generic graphing program does indeed
require the kinds of range finding you're engaged in here.  Feel free to round up to the nearest 100 and
count down by 20s for any graph if you want to hard code a scale.

-Kirby

----------------------------------------------------------------------

'''

import sys

from string import punctuation as punc 

#open the text file to read
f = open(sys.argv[1] , 'r')
text = f.read()
#split string into words
words = text.split()

#function that counts length of a word but skips punctuation
def lenCounter(word):
    wordLength =0
    for c in word:
        if c not in punc:
            wordLength+=1  
    return wordLength

#define dictionary that will hold word length (key) and frequency (value)
freq = {}

#split input file of text into words
words = text.split()

#process each word 
for word in words:
    wordLength = lenCounter(word)
    if wordLength in freq:
        freq[wordLength] += 1
    else:
        freq[wordLength] = 1

#print out dictionary results header
print("{0:<15s} {1:<10s}".format('word length:', 'frequency:'))
#print out dictionary in table format 
for wordLength in sorted((freq.keys())):
    print("{0:<15d} {1:<25d}".format(wordLength,freq[wordLength]))

xMin = min(freq)

xMax = max(freq)

#figure lowest value in y axis
yMin = min(freq.values())

yMax = max(freq.values())

print("--------------------------------------") 
myStepY = round(yMax/10)

for y in range(yMax,0,-myStepY):  # stepping down from yMax to 0 by -myStepY increments
    print ("{:>6} | ".format(y), end="") # suppress newline after label
    for x in range(1,xMax+1):   # iterate through the x values from 1 to xMax
        if freq.get(x,0) >= y:  # if word count > or equal to y value...
            column = "***"
        else:
            column = "   "
        print(column, end="") # again suppress newline
    print() # next row
print("       --------------------------------------")          