class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stk = []

        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stk and t > stk[-1][0]:
                temp, index = stk.pop()
                res[index] = i - index

            # processing happens above

            stk.append((t, i))

        return res
