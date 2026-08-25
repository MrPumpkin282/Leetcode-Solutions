class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        sums = 0
        maxx = nums[len(nums)-1]
        for i in range(0,len(nums)):
            diff = 0
            diff = abs(nums[i] - maxx)
            sums += diff
        return sums
        
        