class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        sums = 0
        median = nums[len(nums) // 2]
        for i in range(0,len(nums)):
            diff = 0
            diff = abs(nums[i] - median)
            sums += diff
        return sums        