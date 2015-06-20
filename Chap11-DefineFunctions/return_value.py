__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
#
def structure_list(text):
    """Returns a list of punctuation & location of 
    the word 'Python' in a sample of text"""
    punctuation_marks = "!?.,:;"
    punctuation = []
    for mark in punctuation_marks:
        if mark in text:
            punctuation.append(mark)
    return punctuation, text.find('Python')

text_block = """\
Python is used everywhere nowadays.
Major users including Google, Yahoo!, CERN and NASA (a team of 40 scientists and engineers
are using Python to test the systems supporting the Mars Space Lander project).
ITA, the company that produces the route search engine? used by Orbitz, CheapTickets,
travel agents and many international and national airlines, uses Python extensively.
This snippet of text taken from chapter 1."""

print(text_block)
print('-'*80) 

#counter for # instances of the word python
counter =0

for line in text_block.splitlines():
    print(line)
    p,l  = structure_list(line)
    if p:
        print("Contains:", p)
    else:
        print("No punctuation in this line of text")
    if ',' in p:
        print("This line contains a comma")
    if '?' in p:
        print("this line contains a question mark.")
    if l >= 0:
        print("Python is first used at {0}".format(l))
        #increment counter
        counter +=counter
        print(counter)
    print('-'*80) 

print('-'*80) 
print("the number of times python was found in the text was: ", counter))
