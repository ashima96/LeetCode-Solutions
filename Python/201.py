class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left <= right//2:
            return 0
        
        res = left
        for num in range(left+1, right+1):
            res = res & num
        return res


left = 5
right = 7
solution = Solution()
print(solution.rangeBitwiseAnd(left, right))