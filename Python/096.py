class Solution:
    def numTrees(self, n: int) -> int:
        N = 2*n
        r = n + 1
        R = n
        res = 1
        while N > 0 and R > 0:
            res = res * N
            N -= 1
            res = res/R
            R -=1
            
        while N > 0 and r > 0:
            res = res * N
            N -= 1
            res = res/r
            r -=1
            
        return round(res)


n = 3
solution = Solution()
print(solution.numTrees(n))