class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        max_profit = 0

        l, r = 0, 1

        while r < len(prices):
            while prices[r] < prices[l]:
                l += 1

            max_profit = max(max_profit, prices[r] - prices[l])


            r += 1 

            


        return max_profit
        