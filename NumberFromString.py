s = 'Algo 978623 ds 1'
stri = list()
stri.append(s)
print(stri)
stri = stri[0].split()
print(stri)
numbers = list()
for i in stri:
    if i.isdigit():
        numbers.append(i)
print(numbers)
a = '9'
for i in numbers:
    if a not in i:
        print(int(i))
    else:
        print(-1)
