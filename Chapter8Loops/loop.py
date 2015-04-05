'''
Created on Feb 21, 2015

@author: jay wilner 3
'''

#===============================================================================
# for i, e in enumerate(range(10, 60, 10)):
#     print(i, e)
# 
# print('\r')
#     
# names = ['John', 'Paul', 'George']
# for i, name in enumerate(names):
#     print('{0}. {1}'.format(i, name))
#     
#===============================================================================

"""Print all factorials less than 1000."""

c = 1
f = 1
while (f < 1000):
    print(f)
    c += 1
    f *= c
    