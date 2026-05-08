class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # return the minimum k that works
        # we need to figure out the formula for ts
        # piles = [1, 4, 3, 2] h = 9 
        

        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            totalTime = 0
            k = (l + r) // 2 # [1, k]

            for p in piles:
                totalTime += math.ceil(p / k)

            if totalTime <= h:
                r = k - 1
                res = min(res, k)
            else:
                l = k + 1

            
            
            
        return res


            
            


            

            

        

    

        

        


        