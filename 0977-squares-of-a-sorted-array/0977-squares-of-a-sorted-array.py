class Solution(object):
    def sortedSquares(self, nums):
        square = 1
        arr = []
        for i in range (len(nums)):
            square = nums[i]*nums[i]
            arr.append(square)
        arr.sort()
        return arr



        