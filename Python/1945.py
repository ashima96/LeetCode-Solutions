class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ""
        for ch in s:
            num += str(ord(ch)-96)
        num = int(num)
    
        while k >0:
            s = 0
            while num > 0:
                s += num%10
                num = num//10
            k -= 1
            num = s
        return num
        

s = "iiii"
k = 1
solution = Solution()
print(solution.getLucky(s, k))