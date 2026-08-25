class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        for i in range(0,int(x*0.5)+1):
            if i*i == x:
                return i
            elif i*i > x:
                return i-1
        return x//2