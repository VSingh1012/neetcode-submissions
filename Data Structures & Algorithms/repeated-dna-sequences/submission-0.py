class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        size = len(s)
        k = 10 # fixed size

        if size <= 10:
            return []

        l = 0
        ssCount = defaultdict(int)
        ssCount[tuple(s[l:k])] += 1  
        res = []      

        for r in range(k, size):
            l += 1
            curr = tuple(s[l : r + 1])
            ssCount[curr] += 1
            if ssCount.get(curr) == 2:
                res.append(s[l:r + 1])


        return res






        






