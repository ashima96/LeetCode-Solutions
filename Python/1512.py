class Solution:
    def numIdenticalPairs(self, nums) -> int:
        goodpairs = 0
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums):
                if i < j and n1 == n2:
                    goodpairs +=1
        return goodpairs
        
        
nums = [1,2,3,1,1,3]
solution = Solution()
print(solution.numIdenticalPairs(nums))