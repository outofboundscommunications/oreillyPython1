__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
#
##!/usr/local/bin/python3
"""Find matching words in two input lines."""

words1 = set(input("Sentence 1: ").lower().split())
words2 = set(input("Sentence 2: ").lower().split())
print("Words in both strings", words1 & words2)
print("Unique to sentence 1:", words1 - words2)
print("Unique to sentence 2:", words2 - words1)