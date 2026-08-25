class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            y = str(n)
            new = 0
            for i in range(len(y)):
                new += int(y[i])**2 
            n = new
        if n == 1:
            return True
        return False
        