class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        for ind in range(len(words)):
            words[ind] = words[ind][::-1]
        return " ".join(words)


s = "Let's take LeetCode contest"
solution = Solution()
print(solution.reverseWords(s))