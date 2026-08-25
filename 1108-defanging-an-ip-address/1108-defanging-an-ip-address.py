class Solution:
    def defangIPaddr(self, address: str) -> str:
        new = ""
        for i in range(0,len(address)):
            if address[i] == ".":
                new += "".join("[.]")
            else:
                new += "".join(address[i])
        return new
        