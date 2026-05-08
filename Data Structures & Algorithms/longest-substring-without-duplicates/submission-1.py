class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # p w w k e w      

        seen = set()

        l, r = 0, 0

        max_length = 0

        while r < len(s) and l <= r:    
            while s[r] in seen and l <= r:
                seen.remove(s[l])
                l += 1  
            # processing happens above         

            seen.add(s[r])            
            
            max_length = max(max_length, (r - l) + 1)

            r += 1

        return max_length

        
                
            
            

        