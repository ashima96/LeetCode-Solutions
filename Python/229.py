class Solution:
    def majorityElement(self, nums):
        n = len(nums)//3
        res = []
        for val in set(nums):
            if nums.count(val) > n:
                res.append(val)
        return res


nums = [3,2,3]
solution = Solution()
print(solution.majorityElement(nums))