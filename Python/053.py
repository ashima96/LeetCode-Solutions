class Solution:
    def maxSubArray(self, nums) -> int:
        maxSum = nums[0]
        currSum = nums[0]
        for num in nums[1:]:
            if currSum < 0:
                currSum = num
            else:
                currSum += num
            maxSum = max(maxSum, currSum)
        return maxSum


nums = [-2,1,-3,4,-1,2,1,-5,4]
solution = Solution()
print(solution.maxSubArray(nums))