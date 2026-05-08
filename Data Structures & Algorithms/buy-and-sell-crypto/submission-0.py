class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            while prices[r] < prices[l]:
                l += 1


            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
            r += 1


        return maxProfit 

            