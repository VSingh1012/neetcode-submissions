class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1


        minimum = float("inf")

        # Get through all the edge cases
        if nums[l] < nums[r] or n == 1: 
            return nums[l]

        if n == 2: 
            return nums[r] if nums[r] < nums[l] else nums[l]

            

        while l <= r:
            m = (l + r) // 2
            if nums[m] < nums[m - 1]:
                return nums[m]
            
            if nums[m] >= nums[l] and nums[m] > nums[r]: 
                l = m + 1
            else:
                r = m

            

                
    








        