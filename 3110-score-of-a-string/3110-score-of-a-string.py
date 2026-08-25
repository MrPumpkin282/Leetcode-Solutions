class Solution:
    def scoreOfString(self, s: str) -> int:
        difference = 0
        sum = 0
        for i in range (0,len(s)-1):
            difference = abs(ord(s[i+1]) - ord(s[i]))
            sum += difference
        return sum 
             
        