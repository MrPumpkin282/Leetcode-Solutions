class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        x = "qwertyuiop"
        y = "asdfghjkl"
        z = "zxcvbnm"
        p = []
        for i in words:
            count1 = 0
            count2 = 0
            count3 = 0
            for j in i:
                if j.lower() in x:
                    count1 += 1
                elif j.lower() in y:
                    count2 += 1
                elif j.lower() in z:
                    count3 += 1
            if count1 == len(i) or count2 == len(i) or count3 == len(i):
                p.append(i)
        return p

            
                
                
                


               
