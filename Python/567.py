from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        cs1 = Counter(s1)
        cs2 = Counter(s2)
        for key, val in cs1.items():
            if key not in cs2.keys() or cs2[key] < val:
                return False 
        for ind in range(len(s2)-len(s1)+1):
            if s2[ind] in s1 and sorted(s2[ind : ind + len(s1)]) == sorted(s1):
                return True
        return False


s1 = "ab"
s2 = "eidbaooo"
solution = Solution()
print(solution.checkInclusion(s1, s2))