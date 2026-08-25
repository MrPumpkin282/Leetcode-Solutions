class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = []
        count = []
        maxx = 0
        for i in range(len(nums)):
            if nums[i] not in temp:
                temp.append(nums[i])
        for i in range(len(temp)):
            s = 0
            for j in range(len(nums)):
                if temp[i] == nums[j]:
                    s += 1
            count.append(s)
        for i in range(len(count)):
            if count[i] > maxx:
                maxx = count[i]
        y = count.index(maxx)
        return temp[y]



            
                

