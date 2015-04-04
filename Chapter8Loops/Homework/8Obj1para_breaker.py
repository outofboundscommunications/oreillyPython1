'''
this is my enumerate branch

Objective 1:
This project tests your ability to use more sophisticated loops.

Create a new Python source file named para_breaker.py.
Write a program to break up a paragraph into sentences and phrases. 
Sentences are delineated by periods
Phrases are delineated by commas.
Print the results to the screen. 
You will need to use a loop within a loop.
Use the text from the second paragraph of the United States Declaration of Independence (provided below).
'''

'''
Overall Comments:
 A gallant attempt but armed with too few power tools for the job.

Just to get going, you can triple quote the paragraph and insert linebreaks where looks
nice, then take them back out again programmatically in one line:

para = para.replace("\n", " ")

Just make sure you slice immediately at the word boundary, no dangling space, and the
above will restore spaces in place of line breaks.  That makes the source code look pretty.

But beyond that, the main hero to the rescue is string.split(string) where you use the 
presence of "." and "," to carve up the one long string into a list of sausage strings,
carved up in turn.  

I.e.

for sentence in para.split("."):

or even, to get the consecutive number for free:

for num, sentence in enumerate(para.split(".")):

and right there you get your number and sentence, inside of which loop, a similar split of sentence on comma "," nets you phrases.  enumerate handy there too.

You're bottom-up character to by character approach is error prone I think.  Think more in terms of using split to get sentences and phrases from sentences.

Hint:  always look at the interactive console as a gymnasium or tool shed where you go to practice interactively with the tools in question.  It's another way of reminding yourself of the API.  Then when you remember, add to the saved source code you're working on.  Back and forth, console, editor, console, editor -- that's a typical workflow when writing Python.  Then run the script you're working on every so often.  And the tests (in Python2 we emphasize writing tests to accompany every project).

-Kirby



'''

#assign the text to a string variable
para='''
We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness. - That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, - That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness. Prudence, indeed, will dictate that Governments long established should not be changed for light and transient causes; and accordingly all experience hath shewn that mankind are more disposed to suffer, while evils are sufferable than to right themselves by abolishing the forms to which they are accustomed. But when a long train of abuses and usurpations, pursuing invariably the same Object evinces a design to reduce them under absolute Despotism, it is their right, it is their duty, to throw off such Government, and to provide new Guards for their future security.  - Such has been the patient sufferance of these Colonies; and such is now the necessity which constrains them to alter their former Systems of Government. The history of the present King of Great Britain is a history of repeated injuries and usurpations, all having in direct object the establishment of an absolute Tyranny over these States. To prove this, let Facts be submitted to a candid world.
'''

#remove line breaks
para = para.replace("\n", " ")
#for num, sentence in enumerate(para.split(".")):
#   print('Sentence number: ',num+1,"-",sentence)
    
for num, sentence in enumerate(para.split(".")):
    print("****************************")
    print('Sentence number: ',num+1,": ")
    for num, phrase in enumerate(sentence.split(",")):
        print('phrase number ', num+1,": ",phrase)
        
    
    