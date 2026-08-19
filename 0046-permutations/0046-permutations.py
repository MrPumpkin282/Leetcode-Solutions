class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        perms = list(permutations(nums))
        return perms

        
        