class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        while len(s) > 0 and len(t) > 0:
            if s[0] == t[0]:
                s = s[1:]
            t = t[1:]
        if len(s) == 0:
            return True
        return False


s = "abc"
t = "ahbgdc"
solution = Solution()
print(solution.isSubsequence(s, t))