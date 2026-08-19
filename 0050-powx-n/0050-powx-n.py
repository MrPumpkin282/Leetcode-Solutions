class Solution:
    def myPow(self, x: float, n: int) -> float:
        product = 1
        if n > 0:
            product = float(x**n)
        else:
            product = float((1/x)**(abs(n)))
        return product


        