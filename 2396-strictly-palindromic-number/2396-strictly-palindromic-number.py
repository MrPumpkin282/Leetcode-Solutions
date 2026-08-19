class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        lmao = []
        for i in range(2,n-1):
            bit = ""
            q = n 
            while q > 0:
                bit += "".join(str(q%i))
                q = q // i 
            lmao.append(bit)
        for j in range(0,len(lmao)):
            count = 0
            for i in range(0,len(lmao[j])):
                if lmao[j][i] == lmao[j][len(lmao[j])-i-1]:
                    count += 1
            if count != len(lmao[j]):
                return False
        return True



        