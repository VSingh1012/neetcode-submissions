class Solution:
    def trap(self, height: List[int]) -> int:
        greatestArea = 0
        maxLefts = [0] * len(height)
        maxRights = [0] * len(height)
        maxLeft = 0
        maxRight = 0
        
        l, r = 0, len(height) - 1

        while l < len(height):
            if l == 0:
                maxLeft = 0
            else:
                maxLeft = max(maxLeft, height[l - 1])
                
            maxLefts[l] = maxLeft
            l += 1

        while r >= 0:
            if r == len(height) - 1:
                maxRight = 0
            else:
                maxRight = max(maxRight, height[r + 1])
            
            maxRights[r] = maxRight
            r -= 1

        for x in range(len(maxRights)):
            currArea = min(maxLefts[x], maxRights[x]) - height[x]

            if currArea < 0:
                currArea = 0
            
            greatestArea += currArea

        return greatestArea

             


        
        