class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2 # To get the midpoint

            # conditions for the binary search
            if target == nums[m]:
                return m
            elif target >= nums[m]:
                l = m + 1  
            else:
                r = m -1 



        return -1 # if everything fails