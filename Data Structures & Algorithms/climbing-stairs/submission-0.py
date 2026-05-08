class Solution:
    def climbStairs(self, n: int) -> int:

        # 1 or 2
        memo = {1 : 1, 2 : 2}

        def dp(x):
            if x in memo:
                return memo[x]     

            memo[x] = dp(x - 2) + dp(x - 1)
            return memo[x]
    

        return dp(n)


        