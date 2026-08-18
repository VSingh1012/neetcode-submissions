class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        res = [None] * n


        for i in range(n):
            j = (i + k) % n
            res[j] = nums[i]
            

        for i in range(n):
            nums[i] = res[i]
        
        
