class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        # helper function 
        def isPeakElement(midpoint) -> bool:
            return (m - 1 < 0 and m + 1 == n) or (m - 1 < 0 and nums[m] > nums[m + 1]) or (m + 1 == n and nums[m] > nums[m - 1]) or (nums[m] > nums[m + 1] and nums[m] > nums[m - 1])

        
        while l <= r:
            m = (l + r) // 2
            if isPeakElement(m):
                return m
            else:
                if (m - 1 >= 0 and m + 1 < n) and nums[m] < nums[m - 1] and nums[m] < nums[m + 1]:
                    if (m - 2 >= 0) and nums[m - 2] > nums[m - 1]:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    if (m - 1 >= 0) and nums[m] < nums[m - 1]:
                        r = m - 1
                    elif (m + 1) < n:
                        l = m + 1

            
            # [1,2,3,1]

            
        



                

