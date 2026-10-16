class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        n = len(prices)
        l = 0

        for r in range(1, n):            
            while prices[r] < prices[l]:
                l += 1
        
            
            maxProfit = max(maxProfit, prices[r] - prices[l])

        return maxProfit 

            


