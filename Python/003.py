class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = set()

        j = 0 
        sub = ""
        while len(s) > 0 and j < len(s):
            if s[j] not in sub:
                sub += s[j]
                j +=1
            else:
                substrings.add(sub)
                s = s[1: ]
                j = 0
                sub = ""
        substrings.add(sub)
        substringlen = set(len(i) for i in substrings)
        return max(substringlen) if len(substringlen) > 0 else 0


s = "abcabcbb"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))