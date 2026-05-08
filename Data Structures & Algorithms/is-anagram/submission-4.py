class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        dict_s, dict_t = {}, {}

        for x in range(len(s)):
            dict_s[s[x]] = 1 + dict_s.get(s[x], 0)
            dict_t[t[x]] = 1 + dict_t.get(t[x], 0)

        
        return dict_t == dict_s