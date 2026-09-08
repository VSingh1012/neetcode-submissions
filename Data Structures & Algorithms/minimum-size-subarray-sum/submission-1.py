class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        # [1,1,2,3,5,5]
        
        curr_min = float("inf")

        for i in range(n):
            j = i + 1
            summ = nums[i]
            while j < n and summ < target:
                summ += nums[j] 
                j += 1
            
            if summ >= target:
                curr_min = min(curr_min, j - i)


        return 0 if curr_min == float("inf") else curr_min


        