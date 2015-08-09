"""
Quiz 1 and 2 questions and answers

"""

"""Quiz 1 """
Question1_1 = "How do you define a class called 'Friend' in Python?"
Answer1_1 = "class Friend: "

Question1_2 = "How do you instantiate 'Friend' as an object, and save it to the variable 'f'? "
Answer1_2 = "f=Friend"

Question1_3 = "How would you add an attribute called 'title' with a value of 'buddy' to the f object \
you created in the previous question?"

Answer1_3 = "f.title = 'buddy'"

""" Quiz 2"""

Question2_1="What is the name of the __xx__ method that lets you represent the value of a class as a string?"

Answer2_1="It is the __str__() method"

Question2_2="Where can you store an instantiated object?"

Answer2_2 = "You can store an instantiated object locally or globally."

#function that prints out each question to the screen

def printQuestion(num,question):
    print(60*'-')
    print('\n', 'Question#:',num)
    print(question,'\n')

def printAnswer(answer):
    print(%s % answer)
    
printQuestion(Question1_1)
printAnswer(Answer1_1)

printQuestion(Question1_2)
printAnswer(Answer1_2)

printQuestion(Question1_3)
printAnswer(Answer1_3)

printQuestion(Question2_1)
printAnswer(Answer2_1)

printQuestion(Question2_2)
printAnswer(Answer2_2)
