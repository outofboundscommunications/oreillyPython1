__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
#
'''
Objective 1:
This project tests your ability to use file objects.

1.Create a new Python source file named inputter.py.
2.Write a program that uses a while loop to accept input from the user (if the user presses Enter, exit the program).
3.Save the input to a file, then print it.
4.Upon starting, the program will display any previous content of the file.

Below is an example of possible output from a first run of the program.

Enter text: Python is fun.
Python is fun.
Enter text: O'Reilly makes good classes.
Python is fun.O'Reilly makes good classes.
Enter text:
Below is an example of possible output from a second run of the program.

Python is fun.O'Reilly makes good classes.
Enter text: The file is saving correctly
Python is fun.O'Reilly makes good classes.The file is saving correctly
Enter text:

'''
#create file to write user input to
input_text = open('user_input.txt','a')
input_text.close()

#use while loop to display/accept input from user
while True:
    user_input = open('user_input.txt','r').readlines()
    if user_input:     
        for line in user_input:
            print(line.strip()) 
    myText = input("Enter text: ")