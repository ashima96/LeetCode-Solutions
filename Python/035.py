class Solution:
    def searchInsert(self, nums, target: int) -> int:
        beg = 0
        end = len(nums)-1
        while beg <= end:
            mid = (end + beg)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                beg = mid+1
            else:
                end = mid -1
        if beg > end:
            return beg
        return end


nums = [1,3,5,6]
target = 5
solution = Solution()
print(solution.searchInsert(nums, target))