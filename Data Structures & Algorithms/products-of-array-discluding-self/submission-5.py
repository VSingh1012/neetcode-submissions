class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newNums = [1] * len(nums)
        prefix = 1
        for x in range(len(nums)):
            newNums[x] = prefix
            prefix *= nums[x]
            
        
        suffix = 1
        for x in range(len(nums)):
            newNums[(len(nums) - 1) - x] = newNums[len(nums) - 1 - x] * suffix
            suffix *= nums[len(nums) - 1 - x]

        
        return newNums