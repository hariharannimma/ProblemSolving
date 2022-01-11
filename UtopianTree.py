n = 1012
a = str(n)
nonzero = []
for i in a:
    i = int(i)
    if i != 0:
        nonzero.append(i)
print(nonzero)
divisabule = []
for i in nonzero:
    if n % i == 0:
        divisabule.append(i)
print(divisabule)
