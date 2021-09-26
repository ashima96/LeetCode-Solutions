class Solution:
    def plusOne(self, digits):
        num = str(int("".join([str(i) for i in digits])) + 1)
        return [int(i) for i in num]     


digits = [1,2,3]
solution = Solution()
print(solution.plusOne(digits))