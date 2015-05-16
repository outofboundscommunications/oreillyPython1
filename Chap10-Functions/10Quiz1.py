'''
Question 1:
How do you:

calculate a non-negative value for any numeric input

'''

'''
Question 2:
calculate the highest value from the objects n1, n2, n3, and n4

'''

'''
Question 3:
round the value 1.3234 to the nearest integer?

'''

''' Answer Question 1 '''
print("Question 1 and Answer")
i = eval(input('input any number or decimal, neg or pos:'))
#convert number into positive value using absValue function
absValue = abs(i)
print('input was: ',i,'abs value is:',absValue)

''' Answer question 2'''
print("Question 2 and Answer")

#Gather user input of numbers
numList =[]
while True:
    numString = input("Enter a number (or Enter to quit): ")
    if not numString:
        break
    #convert string to float
    numf = float(numString)
    #add number to list
    numList.append(numf)

#find maximum value in the list of numbers
highValue = max(numList)

#print list of numbers for user to see
for i, num in enumerate(numList):
    print(i,num)
print('the highest value of this list is:' , highValue)


''' Answer question 3'''
print("Question 3 and Answer")
print('we need to round the value 1.3234 to the nearest integer?')

roundedNum = round(1.3234)
print('the rounded number is: ',roundedNum)
