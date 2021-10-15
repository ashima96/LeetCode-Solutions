class Solution:
    def findGCD(self, nums) -> int:
        minNum = min(nums)
        maxNum = max(nums)
        
        for i in range (minNum, 0, -1):
            if minNum%i == 0 and maxNum%i == 0:
                return i


nums = [2,5,6,9,10]
solution = Solution()
print(solution.findGCD(nums))