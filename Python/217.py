from collections import Counter

class Solution:
    def containsDuplicate(self, nums) -> bool:
        dic = Counter(nums)
        for val in set(dic.values()):
            if val > 1:
                return True
        return False

nums = [1,2,3,1]
solution = Solution()
print(solution.containsDuplicate(nums))