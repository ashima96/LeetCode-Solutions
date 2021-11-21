class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        buy = prices[0]
        for i in range(len(prices)):
            diff = prices[i] - buy
            if diff > profit:
                profit = diff
            if buy > prices[i]:
                buy = prices[i]
        return profit


prices = [7,1,5,3,6,4]
solution = Solution()
print(solution.maxProfit(prices))