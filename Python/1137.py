class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [-1]*(n+1)
        
        if n < 2:
            return n
        if n == 2:
            return 1
        
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1
        
        for ind in range(3, n+1):
            memo[ind] = memo[ind-3] + memo[ind-2] + memo[ind-1]
            
        return memo[n]


n = 4
solution = Solution()
print(solution.tribonacci(n))