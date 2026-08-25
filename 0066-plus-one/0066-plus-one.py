class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        ar = []
        for i in digits:
            num += str(i)
        num = int(num) + 1
        num = str(num)
        for i in num:
            ar.append(int(i))
        return ar



        