n = 5,
k = 3
arr = [4, 2, 6, 1, 10]
numOfInLst = 0
for i in arr:
    if i > k:
        a = i//k
        b = i % k
        c = a+b
        numOfInLst += c
    else:
        numOfInLst += 1
newLst = [[] for i in range(numOfInLst)]
print(newLst)
hmap = dict()
for i in arr:
    if i > k:
        for j in range(i + 1):


"""{1:[1, 2, 3], 2:[4], 3:[1, 2], 4:[1, 2, 3], 5:[4, 5], 6:[1], 7:[1, 2, 3], 8:[4, 5, 6], 9:[7, 8, 9], 10:[10]}
    [[], [], [], [], [], [], [], [], [], []]
    [[1, 2, 3], [4], [1, 2], [1, 2, 3], [4, 5], [1], [1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
"""
