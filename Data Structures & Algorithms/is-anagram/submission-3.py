class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)

        s.sort()
        t.sort()

        if len(s) == len(t):
            for x in range(len(s)):
                if (s[x] != t[x]):
                    return False
        else:
            return False
            
                
        return True