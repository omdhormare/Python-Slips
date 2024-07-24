'''
Write a python program to count repeated characters in a string.
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output: o-4, e-3, u-2, h-2, r-2, t-2
'''

s="thequickbrownfoxjumpsoverthelazydog"

for i in set(s):
       if s.count(i)>1:
           print(i,s.count(i))