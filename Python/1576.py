class Solution:
    def getChar(self, neighbours):
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch not in neighbours:
                return ch
                
    def modifyString(self, s: str) -> str:
        if len(s) == 1 and s[0] == "?":
            return "a"
        elif len(s) == 1:
            return s
        
        for ind in range(len(s)):
            if s[ind] == "?":
                if ind == 0 and s[ind+1] == "?":
                    s = "a" + s[ind +1:]
                elif ind == 0:
                    s = self.getChar(s[ind+1]) + s[ind +1:] 
                elif ind == len(s) -1:
                    s = s[ :ind] + self.getChar(s[ind-1])
                else:
                    s = s[ :ind] + self.getChar(s[ind-1]+s[ind+1]) + s[ind+1:]
        return s


s = "ubv?w"
solution = Solution()
print(solution.modifyString(s))