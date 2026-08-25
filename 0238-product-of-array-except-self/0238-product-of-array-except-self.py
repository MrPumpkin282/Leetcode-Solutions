class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = []
        product = 1
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1

        for num in nums:
            if num != 0:
                product *= num
        for i in range(len(nums)):
            if zero_count > 1:
                temp.append(0)
            elif zero_count == 1:
                temp.append(product if nums[i] == 0 else 0)
            else:
                temp.append(product//nums[i])
        return temp
