class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pairMap = defaultdict(int)
        res = 0
        l, r = 0, 0

        while r < len(s):
            pairMap[s[r]] += 1 

            while (r - l + 1) - max(pairMap.values()) > k:
                pairMap[s[l]] -= 1 
                l += 1

            res = max(res, (r - l + 1))
            r += 1

    
        return res

