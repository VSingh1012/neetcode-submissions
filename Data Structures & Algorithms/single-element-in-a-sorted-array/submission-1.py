class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1



        while l <= r:
            m = (l + r) // 2
            if m - 1 >= 0 and nums[m] == nums[m - 1]:
                if (m - l - 1) % 2 == 1:
                    r = m - 2
                else:
                    l = m + 1
            elif m + 1 < n and nums[m] == nums[m + 1]:
                if (r - m + 1) % 2 == 1:
                    l = m + 2
                else:
                    r = m - 1
            else:
                return nums[m]






        
            




            
                
            