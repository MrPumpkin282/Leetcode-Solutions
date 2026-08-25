class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = []
        for i in range(left,right+1):
            for z in str(i):
                if int(z) == 0 or i % int(z) != 0:
                       break
            else:
                nums.append(i)
                
        return nums
                
