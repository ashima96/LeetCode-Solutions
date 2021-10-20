class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        
        if len(n) <= 3:
            return n
        
        i = len(n) -1
        j = 1
        while i > 0:
            i -=1
            j += 1
            if j%3 == 0:
                n = n[:i] + "." + n[i:]
                j = 0
        return n.strip(".")


n = 123456789
solution = Solution()
print(solution.thousandSeparator(n))