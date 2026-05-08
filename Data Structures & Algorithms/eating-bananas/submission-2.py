class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)

        # options 1 - k 

        res = max(piles) # By default, the max would make the most sense! 

        # 1 2 3 4 

        while l <= r: 
            totalTime = 0
            k = (l + r) // 2
            for p in piles:
                totalTime += math.ceil(p / k)     
            if totalTime > h:
                l = k + 1
            elif totalTime <= h:
                r = k - 1
                res = min(res, k)
        
        
        return res

            
            


        
