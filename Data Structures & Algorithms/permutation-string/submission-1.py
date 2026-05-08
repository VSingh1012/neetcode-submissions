class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        target = self.char_map(s1) # map of the target string
        
        
        l, r = 0, len(s1) - 1

        while l < len(s2) and r < len(s2):
            curr_map = self.char_map(s2[l : r + 1])

            if curr_map == target:
                return True

            l += 1
            r += 1
            
    

            
            


            
        return False


    def char_map(self, input_str) -> list:
        ord_chars = [0] * 26 

        for c in input_str:
            ord_chars[ord(c) - ord("a")] += 1

        return ord_chars

            

            
            

            

            

        