class Solution(object):
    def canAliceWin(self, nums):
        alice = 0
        bob = 0
        for i in range(len(nums)):
            if nums[i] < 10:        
                alice += nums[i]
            else:                  
                bob += nums[i]
        return alice > bob or bob > alice
