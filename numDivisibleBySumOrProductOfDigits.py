arr = [25, 36, 45]
print(arr)
length = len(arr)
res = []
pro = []
count = 0
for ele in arr:
    sum = 0
    for digit in str(ele):
        sum += int(digit)
    res.append(sum)
print(res)
for ele in arr:
    pr = 1
    for digit in str(ele):
        pr *= int(digit)
    pro.append(pr)
print(pro)
for i in range(length):
    if pro[i] == 0:
        pass
    elif arr[i] % res[i] == 0 or arr[i] % pro[i] == 0:
        count += 1
print(count)
