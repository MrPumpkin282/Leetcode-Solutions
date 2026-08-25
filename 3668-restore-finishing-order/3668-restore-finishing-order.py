class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        arr = []
        for i in range(0, len(order)):
            for j in range(0, len(friends)):
                if order[i] == friends[j]:
                    arr.append(order[i])
                    break
        return arr