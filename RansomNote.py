# fails 5 out of 22 test cases

a = input()
b = input()
magazine = a.split()
note = b.split()
notedict = dict()
for i in note:
    if i in magazine:
        notedict[i] = 1
    else:
        notedict[i] = 0
if len(notedict) == len(note):
    print('yes')
else:
    print('no')

# so as the above code is working for only some cases so i did the below code which is not mine by the way

"""from collections import defaultdict

def ransom_note(magazine, ransom):
    dicty = defaultdict(int)
    for word in magazine:
        dicty[word]+=1
    for word in ransom: 
        if dicty[word]==0 : return False 
        dicty[word]-=1
    return True"""
