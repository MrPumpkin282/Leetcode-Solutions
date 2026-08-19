class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        if n <= 0:
            return False
        for x in range(31):
            if 2**x == n:
                return True
            
        return False
        
        