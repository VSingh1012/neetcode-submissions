class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        def reverse(l, r):
            while l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                r -= 1
                l += 1

        reverse(0, n - 1)
        reverse(0, (k % n) - 1)
        reverse(k % n, n - 1)
            
        
