class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        for i in range(len(s)):
            seen = {s[i]}
            count = 1
            for j in range(i+1,len(s)):
                if s[i] != s[j] and s[j] not in seen:
                    seen.add(s[j])
                    count += 1
                else:
                    break
            if count >  max_count:
                max_count = count
        return max_count
        