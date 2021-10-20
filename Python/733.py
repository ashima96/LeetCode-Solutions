class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        dic = {i:[] for i in range(len(image))}
        self.fillColor(image, sr, sc, newColor, image[sr][sc], dic)
        return image
        
    
    def fillColor(self, image, i, j, color, prevVal, dic):
        if i >= 0 and j >= 0 and i < len(image) and j < len(image[0]):
            prev = image[i][j]
            if prev == prevVal and j not in dic[i]:
                image[i][j] = color
                dic[i] = dic[i] + [j]
                self.fillColor(image, i-1, j, color, prev, dic)
                self.fillColor(image, i+1, j, color, prev, dic)
                self.fillColor(image, i, j-1, color, prev, dic)
                self.fillColor(image, i, j+1, color, prev, dic)


solution = Solution()
print(solution.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2))