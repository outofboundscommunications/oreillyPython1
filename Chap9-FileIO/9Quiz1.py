'''
Question 1:
How do you make a file available to your program?
What do you do when you are finished working with the file?

'''

'''
Question 2:

What methods can be used to:

report if a file object is readable?
report if a file object is writable?
return a list of the lines in a file?

'''

''' Answer Question 1 '''

#to open a file for writing
#f = open('myfile.txt','w')
# to open a file for reading
f = open('myfile.txt','r')

#when done with a file you need to close it
#f.close()

    
''' Answer Question 2'''

#what methods can be used to:
#report if file is readable

f.readable()

# if file is writable
f.writable()

#return a list of lines in a file
f = open('myfile.txt','r')
f.readlines()