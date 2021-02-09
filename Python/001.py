class Solution:
    def twoSum(self, nums, target):
        store = set()
        store.add(nums[0])

        for ind in range(1, len(nums)):
            rem = target-nums[ind]
            if rem in store:
                return [nums.index(rem), ind]
            store.add(nums[ind])


nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))
