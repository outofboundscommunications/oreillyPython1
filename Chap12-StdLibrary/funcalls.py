"""Take user input, convert to float, and print
out the number to two decimal places, with commas."""
import functions

while True:
    inval = input("Enter a number: ") 
    if not inval:
        break
    number = float(inval)
    print(functions.commareal("{0:.2f}".format(number)))