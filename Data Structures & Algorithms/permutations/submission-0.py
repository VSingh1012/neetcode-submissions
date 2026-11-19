class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(arr, picked):

            if len(arr) == len(nums):
                res.append(arr.copy())
                return

            for x in range(len(nums)):
                if not picked[x]:
                    arr.append(nums[x])
                    picked[x] = True
                    dfs(arr, picked)
                    arr.pop()
                    picked[x] = False

            
        dfs([], [False] * len(nums))

        
        return res


            
