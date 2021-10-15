class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            s = 0
            while num > 0:
                s += num%10
                num = num//10
            num = s
        return num


num = 38
solution = Solution()
print(solution.addDigits(num))