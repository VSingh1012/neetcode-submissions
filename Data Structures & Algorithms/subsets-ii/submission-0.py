class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(curr, i):
            if i >= len(nums): 
                res.append(curr.copy())
                return 
            curr.append(nums[i])
            dfs(curr, i + 1)
            curr.pop()

            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1


            dfs(curr, j)

        dfs([], 0)


        return res
            

                





