class Solution:
    def sortedSquares(self, nums):
        for ind, val in enumerate(nums):
            nums[ind] = val * val
        
        return sorted(nums)


nums = [-4,-1,0,3,10]
solution = Solution()
print(solution.sortedSquares(nums))