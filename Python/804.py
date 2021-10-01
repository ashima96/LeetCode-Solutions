class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        count = set()
        
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        for word in words:
            mc = ""
            for ch in word:
                mc += codes[ord(ch)-97]
            count.add(mc)
        return len(count)


words = ["gin","zen","gig","msg"]
solution = Solution()
print(solution.uniqueMorseRepresentations(words))