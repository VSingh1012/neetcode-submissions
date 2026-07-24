class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stk = []
        i = 0
        n = len(heights)
        max_area = -1

        while i < n:
            height = heights[i]
            start = i

            while stk and height < stk[-1][1]:
                pair = stk.pop()
                curr_area = pair[1] * (i - pair[0])
                max_area = max(max_area, curr_area)
                start = pair[0]

            stk.append([start, height])
            i += 1 


        while stk:
            pair = stk.pop() 
            curr_area = pair[1] * (i - pair[0])
            max_area = max(max_area, curr_area)
            

        return max_area
                

    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

        