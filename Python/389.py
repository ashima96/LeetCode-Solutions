from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = Counter(s)
        t = Counter(t)
        for k in t:
            if k not in s.keys() or t[k] > s[k]:
                return k


s = "abcd"
t = "abcde"
solution = Solution()
print(solution.findTheDifference(s, t))