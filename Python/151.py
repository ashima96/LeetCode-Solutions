import re

class Solution:
    def reverseWords(self, s: str) -> str:
        s = re.sub(' +', ' ', s.strip()).split(" ")
        return " ".join(s[::-1])


s = "the sky is blue"
solution = Solution()
print(solution.reverseWords(s))