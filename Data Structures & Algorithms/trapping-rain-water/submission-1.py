class Solution:
    def trap(self, height: List[int]) -> int:

        maxLefts = [0] * len(height)
        maxRights = [0] * len(height)

        maxLeft = 0
        maxRight = 0

        greatestAmt = 0
        

        l, r = 1, len(height) - 1

        while l < len(height):
            if l == 0:
                maxLeft = 0
            else:
                maxLeft = max(height[l - 1], maxLeft)
            
            maxLefts[l] = maxLeft
            l += 1

        while r >= 0:
            if r == len(height) - 1:
                maxRight = 0
            else:
                maxRight = max(height[r + 1], maxRight)

            maxRights[r] = maxRight
            r -= 1  

        for i in range(len(height)):
            trapAmt = min(maxLefts[i], maxRights[i]) - height[i]

            if trapAmt < 0:
                greatestAmt += 0
            else: 
                greatestAmt += trapAmt


        return greatestAmt