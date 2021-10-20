class Solution:
    def nextGreaterElement(self, nums1, nums2):
        num2ind = {}
        for ind in range(len(nums2)):
            num2ind[nums2[ind]] = ind
        
        res= []
        for ind, val in enumerate(nums1):
            index = num2ind[val]
            flag = True
            for j in range(index, len(nums2)):
                if nums2[j] > val:
                    res.append(nums2[j])
                    flag = False
                    break
            if flag:
                res.append(-1)
        
        return res


nums1 = [4,1,2]
nums2 = [1,3,4,2]
solution = Solution()
print(solution.nextGreaterElement(nums1, nums2))