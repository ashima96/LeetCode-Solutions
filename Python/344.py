class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        beg = 0
        end = len(s) -1
        while beg < end:
            temp = s[beg]
            s[beg] = s[end]
            s[end] = temp
            beg += 1
            end -= 1
        print(s)


s = ["h","e","l","l","o"]
solution = Solution()
solution.reverseString(s)