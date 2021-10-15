class Solution:
    def restoreString(self, s: str, indices) -> str:
        res = [""]*len(s)
        for ind, val in enumerate(indices):
            res[val] = s[ind]
        return "".join(res)


s = "abc"
indices = [0,1,2]
solution = Solution()
print(solution.restoreString(s, indices))