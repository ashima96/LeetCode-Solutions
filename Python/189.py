class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        rotationNo = n-1-k
        nums[:] = nums[rotationNo+1:] + nums[:rotationNo+1]   
        print(nums) 


nums = [1,2,3,4,5,6,7]
k = 3
solution = Solution()
solution.rotate(nums, k)