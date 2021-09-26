class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        
        m = len(word1)+1
        n = len(word2)+1
        matrix = [[0 for x in range(n)] for x in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    matrix[i][j] = j
                elif j == 0:
                    matrix[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
        return matrix[m-1][n-1]


word1 = "intention"
word2 = "execution"
solution = Solution()
print(solution.minDistance(word1, word2))