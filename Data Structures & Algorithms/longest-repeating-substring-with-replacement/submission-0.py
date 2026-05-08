class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCounts = defaultdict(int) 
        longestLen = 0
        l, r = 0, 0


        while r < len(s):
            charCounts[s[r]] += 1


            while (r - l + 1) - max(charCounts.values()) > k:
                charCounts[s[l]] -= 1
                l += 1

            longestLen = max(longestLen, r - l + 1)
            r += 1


        return longestLen

           

            





