class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        for i in  range(0,len(num)):
            if num[i] == "6":
                num = num.replace("6","9",1)
                break
        num = int(num)
        return num
        