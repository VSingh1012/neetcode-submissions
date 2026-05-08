class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1


        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for x in range(len(nums)):
            res[len(nums) - 1 - x] = res[len(nums) - 1 - x] * postfix 
            postfix *= nums[len(nums) - 1 - x]

        return res