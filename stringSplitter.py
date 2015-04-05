"""Program to split a sentence into words."""

s = '''
We hold these truths to be self-evident, that all men are created equal, that they are endowed by their 
Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness. - That to 
secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, - 
That whenever any Form of Government.
'''
while True:
    pos = 0
    for c in s:
        #if the character is a space
        if c == ",":
            #print the string array from the start (0) up to (but not including) the current position
            print(s[:pos])
            s = s[pos+1:]
            break
        pos += 1
    else:
        print(s)
        break