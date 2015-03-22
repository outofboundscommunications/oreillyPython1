'''
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

#assign the text to a string variable

s='''
We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness. - That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, - That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness. Prudence, indeed, will dictate that Governments long established should not be changed for light and transient causes; and accordingly all experience hath shewn that mankind are more disposed to suffer, while evils are sufferable than to right themselves by abolishing the forms to which they are accustomed. But when a long train of abuses and usurpations, pursuing invariably the same Object evinces a design to reduce them under absolute Despotism, it is their right, it is their duty, to throw off such Government, and to provide new Guards for their future security.  - Such has been the patient sufferance of these Colonies; and such is now the necessity which constrains them to alter their former Systems of Government. The history of the present King of Great Britain is a history of repeated injuries and usurpations, all having in direct object the establishment of an absolute Tyranny over these States. To prove this, let Facts be submitted to a candid world.
'''
print('****************************************\n')
phraseCounter =0
while True:
    pos = 0
    for c in s:
        #if the character is a comma, you have found a phrase
        if c == ",":
            #increment the phrase counter by one
            phraseCounter +=1
            #print out the phrase number and the phrase
            print("Phrase: ", phraseCounter,s[:pos+1])
            #reset the string from (current position +1) forward 
            s = s[pos+1:]
            break
        #else the character isnt a space so increment the position counter by one
        pos += 1
    else:
        print(s)
        print('hello')
        break
    