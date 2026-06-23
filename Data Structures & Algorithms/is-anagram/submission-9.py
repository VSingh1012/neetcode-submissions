class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        mapped_s = [0] * 26
        mapped_t = [0] * 26

        for letter in s:
            mapped_s[ord(letter) - ord('a')] += 1 
        for letter in t:
            mapped_t[ord(letter) - ord('a')] += 1

        for x in range(len(mapped_s)):
            if mapped_s[x] != mapped_t[x]:
                return False

        return True
    