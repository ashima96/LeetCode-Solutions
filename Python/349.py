class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1).intersection(set(nums2)))


nums1 = [1,2,2,1]
nums2 = [2,2]
solution = Solution()
print(solution.intersection(nums1, nums2))