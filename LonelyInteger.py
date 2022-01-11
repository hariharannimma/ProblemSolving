a = [1, 2, 3, 4, 3, 2, 1]
hmap = dict()
for i in a:
    if i not in hmap:
        hmap[i] = 1
    else:
        hmap[i] += 1
for i, j in hmap.items():
    if j == 1:
        print(i)
