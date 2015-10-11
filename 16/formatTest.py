'''
"""Produce a listing of people's names, ages and weights."""
data = [
    ("Steve", 59, 202),
    ("Dorothy", 49, 156),
    ("Simon", 39, 155),
    ("David", 61, 135)]
for name, age, weight in data:
    print("{0:>12s} {1:4d} {2:4d}".format(name, age, weight))

'''
freq = {8: 144, 2: 96, 3: 20}   # simulated word length data {length:#_of_words}

xMin = min(freq)
print('xmin is: ', xMin)
xMax = max(freq)
print('xMax is: ', xMax)

yMin = min(freq.values())
print('ymin is: ', yMin)
yMax = max(freq.values())
print('ymax is: ', yMax)

for i in range(yMax, yMin):
    print(i)