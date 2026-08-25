class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        sums = requests[0]
        for i in range(0,len(requests)-1):
            sums += abs(requests[i] - requests[i+1])
        return sums



        