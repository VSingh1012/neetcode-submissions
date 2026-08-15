class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        def get_lps(pattern: str):
            lps = [0] * len(needle)

            l, i = 0, 1

            while i < len(needle):
                if needle[l] == needle[i]:
                    l += 1
                    lps[i] = l
                    i += 1
                else:
                    if l != 0:
                        l = lps[l - 1]
                    else:
                        i += 1
            
            return lps


        lps_arr = get_lps(needle) # longest prefix suffix array
        
        
        o, j = 0, 0 # i for the needle, j for the haystack

        while o < len(needle) and j < len(haystack):
            if needle[o] == haystack[j]:
                o += 1
                j += 1
                if o == len(needle):
                    index = j - len(needle)
            else:
                if o != 0:
                    o = lps_arr[o - 1]
                else:
                    j += 1


        return index





        