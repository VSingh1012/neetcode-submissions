class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        n = len(people)
        counts = [0] * (max(people) + 1)
        for p in people:
            counts[p] += 1

        # [0,1,1,0,1,1]
        # people: [5,1,4,2]
        # limit: 6
        i = 0

        for x in range(n):
            while counts[i] == 0:
                i += 1
            people[x] = i
            counts[i] -= 1

        l, r = 0, n - 1
        count = 0

        while l <= r:
            if people[r] == limit or people[r] + people[l] > limit:
                r -= 1 
                count += 1
            else:
                count += 1
                r -= 1
                l += 1

        return count
        






            


        

          