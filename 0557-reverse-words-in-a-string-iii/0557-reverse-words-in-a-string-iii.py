class Solution:
    def reverseWords(self, s: str) -> str:
        new = ""
        x = []
        for i in s.split():
            x.append(i)
        for i in range(0,len(x)):
            new += "".join(reversed(x[i])) + ' '
        return new.strip()





        
        