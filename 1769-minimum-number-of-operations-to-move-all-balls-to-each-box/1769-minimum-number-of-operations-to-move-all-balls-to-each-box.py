class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        x = []
        for i in range(0,len(boxes)):
            count = 0
            for j in range(0,len(boxes)):
                if boxes[j] != "0":
                    count += abs(i-j)
            x.append(count)
        return x
                
            




