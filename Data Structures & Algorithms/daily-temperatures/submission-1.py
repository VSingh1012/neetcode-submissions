class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stk = []

        for i, n in enumerate(temperatures):
             # # processing
            while stk and stk[-1][1] < n:
                pair = stk.pop()
                res[pair[0]] = i - pair[0]
            
            
            # [30,38,30,36,35,40,28]

            stk.append([i, n])


            # [index, value]
        return res
            

            

