nums = [4, 1, 2, 1, 2]
nums = [1]
numberCount = dict()
for i in nums:
    if i not in numberCount:
        numberCount[i] = 1
    else:
        numberCount[i] = numberCount[i] + 1
print(numberCount)
for i, j in numberCount.items():
    if j != 2:
        print(i)
