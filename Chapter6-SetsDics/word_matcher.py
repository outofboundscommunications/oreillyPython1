'''
Created on Jan 31, 2015

@author: jay wilner 3
'''
"""Find matching words in two input lines."""


words1 = set(input("Sentence 1: ").lower().split())
words2 = set(input("Sentence 2: ").lower().split())

'''
print("Words in both strings", sorted(words1 & words2))
print("Unique to sentence 1:", sorted(words1 - words2))
print("Unique to sentence 2:", sorted(words2 - words1))
'''
print("Words in both strings", (words1 & words2))
print("Unique to sentence 1:", (words1 - words2))
print("Unique to sentence 2:", (words2 - words1))