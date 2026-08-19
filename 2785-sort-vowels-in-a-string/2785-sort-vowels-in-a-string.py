class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        order = []
        lol = ""
        for i in s:
            if i in vowels:
                order.append(i)
        order = sorted(order)
        for i in s:
            if i not in vowels:
                lol += i
            for j in order:
                if i in vowels:
                    lol += j
                    order.pop(0)
                    break
        return lol
        



        

                
                







        