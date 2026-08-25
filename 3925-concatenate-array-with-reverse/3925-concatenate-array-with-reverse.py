class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        arr = []
        for i in nums:
            arr.append(i)
        for i in range(0,len(nums)):
            arr.append(nums[len(nums)-i-1])
        return arr

        
        