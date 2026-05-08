class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        mapped_ls = [[p, s] for p, s in zip(position, speed)]
        mapped_ls.sort(reverse=True)

        stk = []  

        # mapped_ls = [[7, 1], [4, 2], [1, 2], [0, 1]]
        # times = [3, 3, 4, 10]
        for p, s in mapped_ls:
            # calculate the times necessary to reach the target
            stk.append((target - p) / s)
            if len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop()
                
        return len(stk)

        