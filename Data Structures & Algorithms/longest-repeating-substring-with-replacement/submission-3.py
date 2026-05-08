class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pairMap = defaultdict(int)
        res = 0

        l, r = 0, 0


        # AAABABB k = 1

        
        while r < len(s):
            pairMap[s[r]] += 1

            while (r - l + 1) - max(pairMap.values()) > k: # When sliding window is not currently valid
                pairMap[s[l]] -= 1
                l += 1
            
            res = max((r - l + 1), res)

            r += 1
    
        return res


            