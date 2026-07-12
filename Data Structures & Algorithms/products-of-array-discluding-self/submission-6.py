class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix_arr = [0] * n
        postfix_arr = [0] * n 

        # prefix sum
        prefix = 1
        for i in range(n):
            prefix_arr[i] = prefix
            prefix *= nums[i]
        
        # postfix sum
        postfix = 1
        for i in range(n):
            postfix_arr[i] = postfix
            postfix *= nums[n - i - 1]

        # final loop through
        for i in range(n):
            prefix_arr[i] = prefix_arr[i] * postfix_arr[n - i - 1]
        
        return prefix_arr

        