class Solution:
    def isPalindrome(self, s: str) -> bool:
        x, y = 0, len(s) - 1

        while (x < y): 
            while x < y and not self.isAlpha(s[x]):
                x += 1

            while y > x and not self.isAlpha(s[y]):
                y -= 1

            if s[x].lower() != s[y].lower():
                return False
            
            x += 1
            y -= 1

        return True




    def isAlpha(self, c):
        return ((ord('a') <= ord(c) <= ord('z'))or (ord('A') <= ord(c) <= ord('Z')) or 
        (ord('0') <= ord(c) <= ord('9')))
