from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        if len(nums1) < len(nums2):
            nums1 = Counter(nums1)
            nums2 = Counter(nums2)
        else:
            temp = Counter(nums1)
            nums1 = Counter(nums2)
            nums2 = temp
        
        res = []
        for k in nums1.keys():
            if k in nums2.keys():
                v1 = nums1[k]
                v2 = nums2[k]
                if v1 > v2:
                    res = res + [k for i in range(v2)]
                elif v1 == v2:
                    res = res + [k for i in range(v2)]
                else:
                    res = res + [k for i in range(v1)]
        return res


nums1 = [1,2,2,1]
nums2 = [2,2]
solution = Solution()
print(solution.intersect(nums1, nums2))