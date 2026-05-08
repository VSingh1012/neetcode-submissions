class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        mySet = set()

        for r in range(len(s)):
            
            while s[r] in mySet:
                mySet.remove(s[l])
                l += 1

            w = (r - l) + 1
            longest = max(longest, w)
            mySet.add(s[r])

        
        return longest