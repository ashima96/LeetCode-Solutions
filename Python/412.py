class Solution:
    def fizzBuzz(self, n: int):
        res = []
        for ind in range(1, n+1):
            if ind%3 == 0 and ind%5 == 0:
                res.append("FizzBuzz")
            elif ind%3 == 0:
                res.append("Fizz")
            elif ind%5 == 0:
                res.append("Buzz")
            else:
                res.append(str(ind))
        return res


n = 3
solution = Solution()
print(solution.fizzBuzz(n))