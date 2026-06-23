class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        res = defaultdict(int)

        for n in nums:  
            res[n] += 1

        for n in nums:
            if res[n] > 1:
                return True

        return False
            