class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n-1) + self.fib(n-2)


n = 4
solution = Solution()
print(solution.fib(n))