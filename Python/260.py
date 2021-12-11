from collections import Counter

class Solution:
    def singleNumber(self, nums):
        nums = {k:v for k, v in sorted(Counter(nums).items(), key=lambda item: item[1])}
        keys = list(nums.keys())
        return [keys[0], keys[1]]


nums = [1,2,1,3,2,5]
solution = Solution()
print(solution.singleNumber(nums))