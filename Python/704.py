class Solution:
    def search(self, nums, target: int) -> int:
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
        return -1


nums = [-1,0,3,5,9,12]
target = 9
solution = Solution()
print(solution.search(nums, target))