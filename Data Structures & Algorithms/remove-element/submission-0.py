class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0
        n = len(nums)
        k = 0
        
        for i in range(n):
            j = i + 1
            if nums[i] == val or nums[i] == -1:
                if nums[i] == val:
                    k += 1 # num invalid spotted   `
                while j < n and (nums[j] == val or nums[j] == -1):
                    j += 1
                if j < n:
                    nums[i] = nums[j]
                    nums[j] = -1 

        return (n - k)

                

            
            
