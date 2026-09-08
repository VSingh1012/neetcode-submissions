class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
    
        
        # sliding window approach
        # [2,1,5,1,5,3]

        l = 0 
        curr_min = float("inf") # infinity
        n = len(nums)
        summ = 0

        for r in range(n): 
            summ += nums[r]
            while l <= r and summ >= target:
                if (r - l) + 1 < curr_min: 
                    curr_min = (r - l) + 1
                summ -= nums[l]
                l += 1
        

        

        return 0 if curr_min == float("inf") else curr_min

            
        




            





