class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        l = 0

        for r in range(len(prices)):
            while prices[l] > prices[r]:
                l += 1

            # calculations done here
            if prices[r] != prices[l]:
                res = max(res, prices[r] - prices[l])
            
        return res
            




        