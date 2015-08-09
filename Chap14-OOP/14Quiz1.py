
'Question1 =How do you define a class called 'Friend' in Python?'

'''Answer1:

class Friend: 
   pass



Question #2:
How do you instantiate "Friend" as an object, and save it to the variable "f"?



Answer #2:
f =Friend

Comments:
here you need to treat the class as a "callable" meaning like "with a mouth" ( ). 

obj() is "calling obj" and to give birth to a new instance of type X, one goes new_instance = X() # <--- must __call__

What does this do? It triggers the __init__ of whatever class. __init__ is the "birth process" whereby any Type gives birth to a new one of itself.

Revised Answer #2:

f=Friend()

Question #3:
How would you add an attribute called 'title' with a value of 'buddy' to the f object you created in the previous question?

Answer #3:
setattr(f,'title','buddy')

Comments:
this is correct however awkward as dot notation is so much simpler.

f.xxx = 'yyy' # <--- in this form instead, more readable no?

f.title='buddy'