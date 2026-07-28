class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []

        n = len(asteroids)
        i = 0    

        while i < n: 
            while stk and (i < n) and stk[-1] > 0 and asteroids[i] < 0:
                top = stk[-1]
                if abs(asteroids[i]) > abs(top):
                    stk.pop()
                elif abs(asteroids[i]) == abs(top):
                    stk.pop()
                    i += 1
                else:
                    i += 1

            if i < n:
                stk.append(asteroids[i])
                i += 1

        return stk