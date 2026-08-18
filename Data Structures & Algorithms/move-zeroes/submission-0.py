class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def swap(i, j): # O(1) 
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                j = i + 1
                while j < n and nums[j] == 0:
                    j += 1
                if j < n:
                    swap(i, j) # call our O(1) swap function

