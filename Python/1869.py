class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        long0 = 0
        long1 = 0
        count0 = 0
        count1 = 0
        prev = ""
        
        if len(s) == 1:
            return True if s == "1" else False
                
        for ch in s:
            if ch == "0":
                if prev == "0":
                    count0 +=1
                    long0 = max(count0+1, long0)
                else:
                    prev = ch
                    long0 = max(count0+1, long0)
                    count0 = 0
            else:
                if prev == "1":
                    count1 += 1   
                    long1 = max(count1+1, long1)
                else:
                    prev = ch
                    long1 = max(count1+1, long1)
                    count1 = 0
        return True if long1 > long0 else False
        
        
s = "1101"
solution = Solution()
print(solution.checkZeroOnes(s))