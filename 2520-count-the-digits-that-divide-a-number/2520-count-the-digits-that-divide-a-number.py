class Solution(object):
    def countDigits(self, num):
        count = 0
        for digit in str(num):
          if int(digit) != 0 and int(num) % int(digit) == 0:
                count += 1
            
        return count
          
        