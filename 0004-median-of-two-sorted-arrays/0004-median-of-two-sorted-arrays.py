class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = 0
        new = (nums1+nums2)
        n = len(new)
        for i in range(n):
            for j in range(0,n-i-1):
                if new[j] > new[j+1]:
                    new[j],new[j+1] = new[j+1],new[j]
        if n % 2 == 0:
            m = (new[n//2 - 1] + new[n//2]) / 2
            return m
        else:
            m = new[n//2]
            return m
            
        

        