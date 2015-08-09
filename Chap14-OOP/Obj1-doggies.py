"""
Objective 1:
This project tests more of your understanding of classes and objects.

Create a new Python source file named doggies.py.
Write a class named Dog. Dog's __init__() method should take two parameters, name and breed, in addition to the implicit self.
Bind an empty list to a dogs global variable (dogs should not be an attribute of the Dog class).
Using a while loop, get user input for name and breed. The loop should terminate when the user enters a blank name.
For each name and breed entered, create an instance of the Dog class with name and breed as arguments. Append the object to the dogs list.
Each time around the loop, print the current dogs list (the name and breed of each dog).

notes from instructor after 1st submission:

Good work tackling __str__ which will govern what print(dog) does.  Your version:

    def __str__(self):
        return "Dog Name: %s\nDog Breed: %s" % (self.name, self.breed)

in general terms there's nothing amiss i.e. you're free to represent a dog instance however
you wish, sticking to string output but... 

for this particular project, wouldn't name:breed as in "Rover:Mutt" make the most sense?  

Then it's up to enumerate, as you were starting to use, to supply the consecutive integers.  

That's not a Dog's business anyway (Dogs can't count, we all know that), so just have 
__str__ give that little piece of the puzzle and embellish?  Good approach.

No need for Dog to have any methods beyond __init__ (birth) and __str__ (show me as a string).
That's enough for this project.  

Also, if one didn't bother with __str__ you would still have access to 

dog.name 

and 

dog.breed 

as instance attributes e.g. 

for ...
    print("{0} {1}:{2}".format( )) 

using these as arguments.  

__str__ is icing on the cake more than essential / required.

Good work so far.

-Kirby


"""

#Bind an empty list to a dogs global variable (dogs should not be an attribute of the Dog class).
dogs = []

#Write a class named Dog. Dog's __init__() method should take two parameters, name and breed, in addition to the implicit self.
class Dog:
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def __str__(self):
        return "%s:%s" % (self.name, self.breed)

#Using a while loop, get user input for name and breed. 
while True:
    dogName = input("Provide Dog Name:")
    #The loop should terminate when the user enters a blank name.
    if dogName == '':
        break        
    dogBreed = input("Provide dog breed:")
    #For each name and breed entered, create a Dog object. 
    myDog = Dog(dogName,dogBreed)
    #Append the object to the dogs list
    dogs.append(myDog)
    print("DOGS")
    #for dog in dogs:
    #   print(dog.name,dog.breed)
    for i,dog in enumerate(dogs):
        print("{0}:{1}:{2}".format(i,dog.name,dog.breed))
    print('------------------')
    
    
        
