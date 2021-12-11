class Solution:
    def majorityElement(self, nums) -> int:
        for val in set(nums):
            if nums.count(val) > len(nums)//2:
                return val

nums = [3,2,3]
solution = Solution()
print(solution.majorityElement(nums))