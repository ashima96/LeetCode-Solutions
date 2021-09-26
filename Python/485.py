class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        long1 = 0
        count1 = 0
        prev = ""
        
        if len(nums) == 1:
            return 1 if nums[0] == 1 else 0
        if len(set(nums)) == 1:
            return len(nums) if nums[0] == 1 else 0
                
        for n in nums:
            if n == 0:
                prev = n
                long1 = max(count1+1, long1)
            else:
                if prev == 1:
                    count1 += 1   
                    long1 = max(count1+1, long1)
                else:
                    prev = n
                    long1 = max(count1+1, long1)
                    count1 = 0
        return long1


nums = [1,1,0,1,1,1]
solution = Solution()
print(solution.findMaxConsecutiveOnes(nums))