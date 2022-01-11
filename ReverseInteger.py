class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        summ = 0
        sign = 1
        if x < 0:
            sign = -1
            x *= -1
        while x > 0:
            rem = x % 10
            summ = summ * 10 + rem
            x = x // 10
        if not -2147483648 < summ < 2147483648:
            return 0
        else:
            return sign*summ
