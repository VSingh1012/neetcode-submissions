class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowered_s = s.lower()
        left = 0
        right = len(s) - 1

        while left < right:
            while (left < right) and not self.isAlpha(lowered_s[right]):
                right -= 1
            while (left < right) and not self.isAlpha(lowered_s[left]):
                left += 1

            # ?va??
            

            if lowered_s[right] != lowered_s[left]:
                return False
            
            right -= 1
            left += 1

        return True
            



    def isAlpha(self, c):
        # use the ascii values to check this out
        return ('0' <= c <= '9') or ('a' <= c <= 'z')


            



        