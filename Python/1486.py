class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = start
        for i in range(1, n):
            res = res ^ start+2*i
        return res
        

n = 5
start = 0
solution = Solution()
print(solution.xorOperation(n, start))