class Solution:
    def numberOfMatches(self, n: int) -> int:
        num_of_matches = 0
        while n > 1:
            if n%2 == 0:
                num_of_matches += n//2
                n = n//2
            else:
                num_of_matches += (n-1)//2
                n = (n-1)//2 +1
        return num_of_matches


n = 7
solution = Solution()
print(solution.numberOfMatches(n))