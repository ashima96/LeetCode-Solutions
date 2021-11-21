class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_str = ""
        for ch in s:
            if ch.isalnum():
                new_str += ch
                
        while len(new_str) > 0:
            if new_str[0] == new_str[len(new_str)-1]:
                new_str = new_str[1:len(new_str)-1]
            else:
                break
                
        if len(new_str) == 0:
            return True
        return False  


s = "A man, a plan, a canal: Panama"
solution = Solution()
print(solution.isPalindrome(s))