i = 20
j = 23
k = 6
actualnum = list()
reversed = list()
length = len(actualnum)
count = 0
for num in range(i, j+1):
    actualnum.append(num)
    num = str(num)
    num = num[::-1]
    num = int(num)
    reversed.append(num)
print(actualnum)
print(reversed)
result = map(lambda x, y: abs(x - y), actualnum, reversed)
a = list(result)
print(a)
for i in a:
    if i % k == 0:
        count += 1
print(count)
