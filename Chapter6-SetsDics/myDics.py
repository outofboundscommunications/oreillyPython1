'''
Created on Jan 31, 2015

@author: jay wilner 3
'''
d = {'Steve': 'Python', 'Peter': 'Perl', 'Rob': 'Ruby'}
print(d)

d[(1, 2)] = "Tuple"
d[1] = "Integer"
print(d)
print('printing the keys of the dic')
for k in d.keys():
    print(k)
print('iterating thru the dic keys and values')
for k in d.items():
    print(k)
print('another method to iterate thru')
for k,v in d.items():
    print (k,'corresponds to',v)
print