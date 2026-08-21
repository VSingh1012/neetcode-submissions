class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        l, r = 0, n - 1 # left and right pointers
        count = 0
        people.sort() # O(nlog(n))

        
        while l <= r:
            while l <= r and (people[r] == limit or people[r] + people[l] > limit):
                r -= 1
                count += 1        
            if l <= r:
                count += 1
                r -= 1
                l += 1

        return count
        
          




                
