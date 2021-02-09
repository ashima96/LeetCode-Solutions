class Solution:
    def reverse(self, x):
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)

        reverse = 0
        while x > 0:
            reverse = reverse * 10 + x % 10
            if reverse >= pow(-2, 31) and reverse < pow(2, 31):
                x = x // 10
            else:
                return 0
        return sign * reverse


y = 123
solution = Solution()
print(solution.reverse(y))
