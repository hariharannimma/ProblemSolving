"""grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
count = 0
for i in grid:
    print(i)
for i in grid:
    for j in i:
        if j == 1:
            count += 1
print(count)
count *= 4
print(count)
for i in range(len(grid)):
    for j in range(len(grid[i]) - 1):
        if grid[i][j] == grid[i][j+1] and grid[i][j]:
            count -= 1
print(count)
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == grid[j][i]:
            count -= 1
print(count)"""
n = 8
m = 6
a1 = [12, 23, 34, 45, 56, 67, 78, 89]
a2 = [23, 11, 45, 56, 99, 78]
r = []


def s(a1, a2):
    for i in a1:
        for j in a2:
            if i == j:
                r.append(i)
    print(*r)


print(s(a1, a2))
"""r = dict()
c = []
for i in a1:
    if i not in r:
        r[i] = 1
    else:
        r[i] += 1
for i in a2:
    if i not in r:
        r[i] = 1
    else:
        r[i] += 1
print(r)
for i, j in r.items():
    if j == 2:
        c.append(i)
print(c)"""
