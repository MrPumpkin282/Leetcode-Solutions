class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_len = 0
        length = 0
        for i in range(0,len(sentences)):
            words = sentences[i].split()
            length = len(words)
            if length > max_len:
               max_len = length
        return max_len

        