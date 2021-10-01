class Solution:
    def getConcatenation(self, nums):
        res = [0]*(2*len(nums))
        for i in range(len(nums)):
            res[i] = nums[i]
            res[i+len(nums)] = nums[i]
        return res


nums = [1,2,1]
solution = Solution()
print(solution.getConcatenation(nums))