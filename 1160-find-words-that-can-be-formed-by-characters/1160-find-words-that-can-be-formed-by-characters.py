class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum = 0
        for i in range(0,len(words)):
            count = 0
            for j in words[i]:
                if words[i].count(j) <= chars.count(j):
                    count += 1
            if count == len(words[i]):
                sum += len(words[i])
        return sum
            
        