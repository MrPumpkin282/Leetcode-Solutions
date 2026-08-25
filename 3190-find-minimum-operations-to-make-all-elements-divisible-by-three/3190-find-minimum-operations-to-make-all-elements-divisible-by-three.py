class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
       count = 0 
       for i in range(0,len(nums)):
          if nums[i] % 3 != 0 and (nums[i]+1)%3 != 0:
            nums[i] = nums[i] - 1
            count += 1
          elif nums[i] % 3 != 0 and (nums[i]-1)%3 != 0:
            nums[i] = nums[i]+1
            count += 1
          if nums[i] % 3 == 0:
            count += 0
       return count
            

        