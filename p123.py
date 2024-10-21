s="thequickbrownfoxjumpsoverthelazydog"

for i in set(s):
    if s.count(i)>1:
        print(i,s.count(i))