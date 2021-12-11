class Solution:
    def missingNumber(self, nums) -> int:
        nums = sorted(nums)
        for i in range(len(nums)+1):
            if i == len(nums) or i != nums[i]:
                return i


nums = [3,0,1]
solution = Solution()
print(solution.missingNumber(nums))