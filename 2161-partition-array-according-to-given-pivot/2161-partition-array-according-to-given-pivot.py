class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        new = []
        for i in range(0,len(nums)):
            if nums[i] < pivot:
                new.append(nums[i])
        for i in range(0,len(nums)):
            if nums[i] == pivot:
                new.append(nums[i])
        for i in range(0,len(nums)):
            if nums[i] > pivot:
                new.append(nums[i])
        return new
            
            


        

        