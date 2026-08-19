class Solution(object):
    def subtractProductAndSum(self, n):
        digits = []
        sum = 0
        product = 1
        difference = 0
        for i in str(n):
            digits.append(int(i))
        for j in (digits):
            sum += j
            product *= j
        difference = product - sum
        return difference

        
        
        