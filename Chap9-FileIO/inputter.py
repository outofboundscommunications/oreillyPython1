
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
#create file to store user input
input_text = open('C:\\Users\\jay wilner 3\\workspace\\oreillyPython1\\Chap9-FileIO\\myuser_input.txt','a')
#input_text = open('user_input.txt','a')
input_text.close()

#upon starting the program displays any previous content of the file 
user_input = open('C:\\Users\\jay wilner 3\\workspace\\oreillyPython1\\Chap9-FileIO\\myuser_input.txt','r').readlines()
if user_input:     
    for line in user_input:
        print(line.strip())

#now capture user input           
while True:
    f = open('C:\\Users\\jay wilner 3\\workspace\\oreillyPython1\\Chap9-FileIO\\myuser_input.txt','a')
    i = input("Enter text (or Enter to quit): ")
    if not i:
        break
    #append phrase to file
    f.write(i)
    f.write('\n')
    f.close()
    #open file again for reading/printing out last element
    f = open('C:\\Users\\jay wilner 3\\workspace\\oreillyPython1\\Chap9-FileIO\\myuser_input.txt','r')
    myTextString =""
    #read contents of file into a list
    myList = f.readlines()
    #iterate thru the list to make a string to print out on one line
    for item in myList:
        #remove the line breaks in the item
        myItem = item.strip()
        myTextString += myItem
    print(myTextString)
    
print('the program has exited and the file has been closed')
f.close()
