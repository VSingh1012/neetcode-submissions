class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        n = len(s) # arbitrary
        s_map = [0] * 26
        t_map = [0] * 26

        for x in range(n):
            s_map[ord(s[x]) - ord('a')] += 1
            t_map[ord(t[x]) - ord('a')] += 1

        map_length = len(s_map)

        for x in range(map_length):
            if s_map[x] != t_map[x]:
                return False

        return True
        