class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        x = str(n)
        sums = 0
        for i in x:
            sums += int(i)
        return sums


            


        