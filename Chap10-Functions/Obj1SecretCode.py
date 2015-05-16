
'''
Objective 1:
This project requires you to use built-in functions to perform character manipulations.

8788684

1. Create a new Python source file named secret_code.py.
2. Write a program to read a line of input from the user, and encode it using the following cipher:
3. Take each character of the string individually, and make the corresponding character in the output string be 
that whose ordinal value is 1 more than the ordinal value of the input character. 
4. Once the output string has been constructed in this way, the output of the program should be the 
reverse of the constructed output string.
5. Below is an example of possible input and output from running the program.

Message: This is it
uj!tj!tjiU

'''

i = input("input a phrase or sentence:")
cipherPhrase =""
for c in i:
    #print('the character is:',c)
    newC = chr(ord(c)+1)
    #print('the ciphered character is:',newC)
    cipherPhrase+=newC
print('the input phrase was:', i)
print('the ciphered phrase is:', cipherPhrase)
    
  
    

