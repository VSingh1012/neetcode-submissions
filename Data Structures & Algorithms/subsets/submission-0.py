class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # end condition, where you return the value

        res = []

        def backtrack(index, subset):
            if index == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[index])
            backtrack(index + 1, subset)
            subset.pop()

            backtrack(index + 1, subset)

        
        backtrack(0, [])

        return res

    
        