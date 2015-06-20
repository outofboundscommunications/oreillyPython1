
__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
#

text_block = """\
Python is used everywhere nowadays.
Major users including Google, Yahoo!, CERN and NASA (a team of 40 scientists and engineers
are using Python to test the systems supporting the Mars Space Lander project).
ITA, the company that produces the route search engine used by Orbitz, CheapTickets,
travel agents and many international and national airlines, uses Python extensively.
The YouTube video presentation system uses Python almost exclusively, despite their
application requiring high network bandwidth and responsiveness.
This snippet of text taken from chapter 1."""

print(text_block)
print('-'*80) 
for line in text_block.split('\n'):
    print(line)
