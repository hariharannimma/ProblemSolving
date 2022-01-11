# recursion of is happy while true only and its a wrong problem anyway
# we need to think a other way
# link is https://leetcode.com/problems/happy-number/


def isHappy(n):
    num = set()
    while(1):
        res = 0
        while n > 0:
            a = n % 10
            n = n//10
            res += a*a
        if res == 1:
            return True
        elif res not in num:
            num.add(res)
            n = res
        else:
            return False


n = int(input('Enter a number'))
a = isHappy(n)
print(a)
