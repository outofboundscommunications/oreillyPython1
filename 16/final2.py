freq = {2:144, 6:75, 8:42}  # simulated word length data {length:#_of_words}

#print out dictionary results header
print("{0:<15s} {1:<10s}".format('word length:', 'frequency:'))
#print out dictionary in table format 
for wordLength in sorted((freq.keys())):
    print("{0:<15d} {1:<25d}".format(wordLength,freq[wordLength]))

xMin = min(freq)
print('xMin is: ',xMin)

xMax = max(freq)
print('xMax is: ',xMax)

#figure lowest value in y axis
yMin = min(freq.values())
print('yMin is: ',yMin)

yMax = max(freq.values())
print('yMax is: ', yMax)

myStepY = round(yMax/10)
print('myStepY is: ',myStepY)

for y in range(yMax,0,-m):  # stepping down from yMax to 0 by -10 increments
    print ("{:>6} | ".format(y), end="") # suppress newline after label
    for x in range(1,xMax+1):   # needs wider range for longer word lengths
        if freq.get(x,0) >= y:  # if word count > or equal to y value...
            column = "***"
        else:
            column = "   "
        print(column, end="") # again suppress newline
    print() # next row
print("       --------------------------------------")                   