from collections import Counter

class Solution:
    def singleNumber(self, nums) -> int:
        nums = Counter(nums)
        for k in nums:
            if nums[k] == 1:
                return k


nums = [2,2,1]
solution = Solution()
print(solution.singleNumber(nums))