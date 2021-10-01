class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        ind = word.index(ch)
        return word[:ind+1][::-1]+word[ind+1:]


word = "abcdefd"
ch = "d"
solution = Solution()
print(solution.reversePrefix(word, ch))