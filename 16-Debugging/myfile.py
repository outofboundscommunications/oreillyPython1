__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.

#this is my test file where i import the declaration of independence text file
#break into lines, etc.
#the function needs to take in the file name as an argument

#open the declaration file to read
f = open('declaration.txt', 'r')

#read content of file into a single string into variable
text = f.read()

#split string into words
words = text.split()
for word in words:
    print(word)
    