class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        upper = set()
        for i in word:
            if i.islower():
                lower.add(i)
            else:
                upper.add(i)
        count = 0
        for sp in lower:
            if sp.upper() in upper:
                count += 1
        return count
            