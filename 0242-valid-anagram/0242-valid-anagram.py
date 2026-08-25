class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = 0
        for i in s:
            if s.count(i) == t.count(i):
                count += 1
        if count ==  len(s):
            return True
        else:
            return False


            
              
        