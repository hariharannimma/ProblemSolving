numberCount = dict()
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
for i in ar:
    if i not in numberCount:
        numberCount[i] = 1
    else:
        numberCount[i] = numberCount[i] + 1
print(numberCount)
result = []
count = 0
for i in numberCount.values():
    if i > 1:
        i = i//2
        result.append(i)
print(result)
