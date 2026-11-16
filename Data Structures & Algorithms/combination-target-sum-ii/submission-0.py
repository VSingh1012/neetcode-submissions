class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []


        def dfs(i, arr, curr_sum):
            if curr_sum == target:
                res.append(arr.copy())
                return
            elif i >= len(candidates) or curr_sum > target:
                return 

            arr.append(candidates[i])
            curr_sum += candidates[i]
            # now call recursion
            dfs(i + 1, arr, curr_sum)

            # backtrack 
            arr.pop()
            curr_sum -= candidates[i]

            j = i + 1

            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1

            

            # don't include current number
            dfs(j, arr, curr_sum)            


        dfs(0, [], 0)

        return res