class Solution(object):
    def arraySign(self, nums):
        def signFunc(x):
            if x > 0:
                return 1
            elif x < 0:
                return -1
            else:
                return 0
        x = 1
        for i in range (len(nums)):
            x *= nums[i]
        return signFunc(x)

                  