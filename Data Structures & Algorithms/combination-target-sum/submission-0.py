class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combination = [] # good practice

        def backtracking(curr_sum, index):
            if curr_sum == target:
                res.append(combination.copy())
                return 
            if curr_sum > target or index == len(nums): # we've reached the end without adding anything, so nothing worked
                return         

            # 1: use the current number
            # 2: find a different number on a different index
            curr_sum += nums[index]
            combination.append(nums[index])
            backtracking(curr_sum, index) # run our backtracking 
            # reverse the changes here
            curr_sum -= nums[index]
            combination.pop()

            # option 2: find a different number
            backtracking(curr_sum, index + 1)

        

        backtracking(0, 0)


        return res


            

        