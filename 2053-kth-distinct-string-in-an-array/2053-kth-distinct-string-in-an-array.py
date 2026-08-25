class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = 0
        x = []
        for i in range(0,len(arr)):
            if arr.count(arr[i]) == 1:
                x.append(arr[i])
        if len(x) >= k:
            return x[k-1]
        return ""
                    
                


        