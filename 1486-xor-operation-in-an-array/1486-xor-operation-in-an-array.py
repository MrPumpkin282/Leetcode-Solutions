class Solution(object):
    def xorOperation(self, n, start):
        num = []
        result = 0
        for i in range(0,n):
            num.append(start + 2 * i)
        for x in num:
            result ^= x

        return result