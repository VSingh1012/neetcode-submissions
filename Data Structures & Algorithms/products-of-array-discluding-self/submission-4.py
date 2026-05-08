class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for x in range(len(nums)):
            res[x] = prefix
            prefix *= nums[x]

        postfix = 1

        for o in range(len(nums)):
            res[(len(nums) - 1) - o] *= postfix
            postfix *= nums[(len(nums) - 1) - o]
        

        return res