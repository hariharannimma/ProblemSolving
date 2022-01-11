d1, m1, y1 = 14, 7, 2018
d2, m2, y2 = 5, 7, 2018
fine = 0
days = 0
if y1 <= y2 and m1 <= m2 and d1 <= d2:
    print(fine)
elif y1 <= y2 and m1 <= m2:
    fine = 15 * (d2-d1)
    print(fine)
elif y1 <= y2:
    if m1 == 1:
        days = 31
    elif m1 == 2:
        days = 31 + 28
    elif m1 == 3:
        days = 31 + 28 + 31
    elif m1 == 4:
        days = 31 + 28 + 31 + 30
    elif m1 == 5:
        days = 31 + 28 + 31 + 30 + 31
    elif m1 == 6:
        days = 31 + 28 + 31 + 30 + 31 + 30
    elif m1 == 7:
        days = 31 + 28 + 31 + 30 + 31 + 30 + 31
    elif m1 == 8:
        days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
    elif m1 == 9:
        days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30
    elif m1 == 10:
        days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
    elif m1 == 11:
        days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
    else:
        days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
    if (m1 % 4 == 0) and (m1 % 100 != 0) or (m1 % 400 == 0):
        days += 1
    else:
        days = days
    fine = 500 * (days - ())
