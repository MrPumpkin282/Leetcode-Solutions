class Solution(object):
    def addDigits(self, num):
        while num >= 10:         
            add = 0               
            for i in str(num):
                add += int(i)
            num = add
        return num
