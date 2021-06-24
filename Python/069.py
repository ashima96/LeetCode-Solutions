import math

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))
    

x = 8
solution = Solution()
print(solution.mySqrt(x))