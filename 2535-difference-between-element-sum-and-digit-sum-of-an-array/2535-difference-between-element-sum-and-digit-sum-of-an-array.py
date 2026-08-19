class Solution(object):
    def differenceOfSum(self, nums):
        element_sum = 0
        digit_sum = 0
        difference = 0
        for i in (nums):
            element_sum += i
        for d in nums:
            for digit in str(d):
                 digit_sum += int(digit)
            
        difference = element_sum - digit_sum
        return difference

        