class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res = []                         

        def dfs(curr_sum, arr, i):
            if curr_sum == target:
                res.append(arr.copy())
                return
            elif i >= len(nums) or curr_sum > target:
                return

            arr.append(nums[i])
            curr_sum += nums[i]
            dfs(curr_sum, arr, i)
            # backtrack 
            arr.pop()
            curr_sum -= nums[i]

            # skip 
            dfs(curr_sum, arr, i + 1)


            
        

        
        dfs(0, [], 0)

        return res
