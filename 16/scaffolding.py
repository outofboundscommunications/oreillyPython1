freq = {8: 144, 2: 96, 3: 20}   # simulated word length data {length:#_of_words}

xMin = min(freq)
xMax = max(freq)

#figure lowest value in y axis
yMin = min(freq.values())
yMax = max(freq.values())

for y in range(yMax,-1,-10):  # stepping down from 120 to 10 by -10 increments
    print ("{:>6} | ".format(y), end="") # suppress newline after label
    for x in range(1,xMax+1):   # needs wider range for longer word lengths
        if freq.get(x,0) >= y:  # if word count > or equal to y value...
            column = "*** "
        else:
            column = "    "
        print(column, end="") # again suppress newline
    print() # next row
print("       --------------------------------------")