class Solution:
    def isHappy(self, n: int) -> bool:
        processed_num = set()
        while n > 1 and n not in processed_num:
            processed_num.add(n)
            s = 0
            while n > 0:
                last = n%10
                n = n//10
                s += last * last
            n = s
        if n == 1:
            return True
        return False


n = 19
solution = Solution()
print(solution.isHappy(n))