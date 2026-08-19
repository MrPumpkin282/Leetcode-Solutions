class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        sums = 0
        count = 0
        costs.sort()
        for i in range(len(costs)):
            if sums + costs[i] > coins:
                break
            sums += costs[i]
            count += 1
        return count

         


        