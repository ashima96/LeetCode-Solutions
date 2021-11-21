class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dic = {0:0, 1:0, 2:0}
        for c in nums:
            dic[c] += 1
        i = 0
        j = 0
        while i < len(nums):
            if dic[j] > 0:
                nums[i] = j
                i += 1
                dic[j] = dic[j] - 1
            else:
                j += 1
        print(nums)


nums = [2,0,2,1,1,0]
solution = Solution()
solution.sortColors(nums)