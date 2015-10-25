__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
#
'''
Question 1:
What is "agile" programming?

Question 2:
Why is testing so important?

Question 3:
How can Python help you test your code?

'''

print('Question #1: What is "agile" programming?')
print('"Agile Programming" is based on a set of principles as outlined here:\' )
print('\
     (1)Design and code are test-driven& should proceed in small \
     increments—never add two features at the same time.\
    (2)Integrate continuously & run the system tests to make sure that your \
    change has not had any unintended consequences.\
    (3) Refactor mercilessly: To refactor mercilessly means that if tasks are performed \
      similarly in two places, move them around so theyre done in one place instead, \
      & after each change, rerun \
      all of your tests to verify that your code has not been broken during the refactoring \
      process.\
    (4)Release early and often: Release your program to the users before adding too many \
    features. You can use their feedback to guide further development, \
    and deliver the most important functions of your program faster.\
    (5) Keep it simple.\
    (6) Code is not owned: Agile programming is a team effort, so it is "our code." \
    Never fear changing code created by someone else—its yours to use and testing \
    will help you make sure you dont break it.
    ')
print('Question #2: Why is testing so important?')
print('Testing is valuable because it allows you to check for errors in your code\
    before your code is deployed. By using the doctest module you can add\
    test data in the docstrings so that other developers can work on your code\
    and be able to ensure any features they add dont break existing code.Testing is just \
    as important as the development.')
print("Question 3: How can Python help you test your code?")
print('Python has the doctest module that allows works by embedding executable Python \
    statements and their expected outcomes into the docstrings that are embedded into \
    all Python code. These statements can be read by testing framework software\
    to test your code.')
