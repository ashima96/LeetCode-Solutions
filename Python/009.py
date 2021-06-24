class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            rev = 0
            n = x
            while x > 0:
                rev = rev * 10 + x%10
                x = x//10
            if n == rev:
                return True
            return False
        return False
        
    
x = 121
solution = Solution()
print(solution.isPalindrome(x))

x = -121
print(solution.isPalindrome(x))