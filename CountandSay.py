def countAndSay(x: int, n: int):

    a = str(x)
    if len(a) == n:
        return str(n)
    else:
        x = str(x)
        numbercount = dict()
        for i in x:
            i = int(i)
            if i not in numbercount:
                numbercount[i] = 1
            else:
                numbercount[i] += 1
        a = 0
        b = list()
        for i, j in numbercount.items():
            a = j * 10 + i
            b.append(a)
        b = ''.join(map(str, b))
        b = int(b)
        return countAndSay(b)


n = 2
x = 1
print(countAndSay(x, n))