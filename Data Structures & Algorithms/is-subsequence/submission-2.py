class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s and t or not s and not t:
            return True
        elif not t and s:
            return False

        sn = len(s)
        tn = len(t)

    
        l, r = 0, sn - 1
        l1, r1 = 0, tn - 1

        while l <= r and l1 <= r1:
            while l1 <= r1 and l <= r and t[l1] != s[l]:
                l1 += 1
            while l1 <= r1 and l <= r and t[r1] != s[r]:
                r1 -= 1

            if l1 <= r1:
                l += 1
                l1 += 1
                r -= 1
                r1 -= 1
            
        return True if l > r else False

             
        