class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        x = []
        y = []
        for i in range(1,n+1):
            x.append(i)
        for j in range(len(x)):
            if x[j] % 3 == 0 and x[j] % 5 == 0:
                y.append("FizzBuzz")
            elif x[j] % 3 == 0:
                y.append("Fizz")
            elif x[j] % 5 == 0:
                y.append("Buzz")
            else:
                y.append(str(x[j]))
        return y

        