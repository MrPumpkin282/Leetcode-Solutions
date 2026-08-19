class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        maxx = 0
        for i in range(len(arr)):
            if arr[i] > maxx:
                maxx = arr[i]
        for i in range(0,len(arr)):
            if arr[i] == maxx:
                return i