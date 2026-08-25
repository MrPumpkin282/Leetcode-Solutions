class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x = []
        nums_set = set(nums)
        max = nums[-1]
        for i in range(1,len(nums)+1):
            if i not in nums_set:
                x.append(i)
        return x
        
        

           


        