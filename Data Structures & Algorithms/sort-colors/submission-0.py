class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        counts = [0] * 3 # for each color technically O(1) space 

        for num in nums: # O(n) time complexity
            counts[num] += 1

        i, j = 0, 0 # O(1)

        while i < n: # O(n)   
            while counts[j] == 0:
                j += 1 
            if nums[i] != j:
                nums[i] = j

            counts[j] -= 1
            i += 1


