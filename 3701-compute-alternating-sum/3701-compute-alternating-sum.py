class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        sums = nums[0]
        for i in range(1,len(nums)):
            if i%2 == 0:
                sums += nums[i]
            else:
                sums -= nums[i]
        return sums

        