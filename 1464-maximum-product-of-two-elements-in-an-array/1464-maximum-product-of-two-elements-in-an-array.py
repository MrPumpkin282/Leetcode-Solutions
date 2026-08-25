class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i]-1)*(nums[j]-1) > maxx and i != j:
                    maxx = (nums[i]-1)*(nums[j]-1)
        return maxx
        