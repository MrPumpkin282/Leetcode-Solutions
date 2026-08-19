class Solution:
    def maxDistinct(self, s: str) -> int:
        x = []
        for i in s:
            if i not in x:
                x.append(i)
        y = len(x)
        return y
            