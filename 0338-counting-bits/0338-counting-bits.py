class Solution:
    def countBits(self, n: int) -> List[int]:
        x = []
        for i in range(n+1):
            count = 0
            bit = bin(i)
            for j in str(bit):
                if j == '1':
                  count += 1
            x.append(count)
        return x
        