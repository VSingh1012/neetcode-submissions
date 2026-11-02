class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:


        
        slen = len(s)
        plen = len(p)

        if plen > slen:
            return []

        pMap = defaultdict(int) # all entries when initialized have default values of 0 
        sMap = defaultdict(int)
        l = 0

        # initialize pCount's hashmap as well as sCount so we can start moving the pointers

        for i in range(plen):
            pMap[p[i]] += 1 
            sMap[s[i]] += 1

        res = [0] if pMap == sMap else []

        # start from where we left off on the plen'th iteration
        for r in range(plen, slen):
            sMap[s[l]] -= 1
            if sMap.get(s[l], 0) == 0:
                sMap.pop(s[l]) 
            l += 1
            # add the new
            sMap[s[r]] += 1
            
            if sMap == pMap:
                res.append(l)


        return res




        




