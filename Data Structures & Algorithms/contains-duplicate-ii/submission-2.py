class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        n = len(nums)

        seen = {}

        for i, val in enumerate(nums):
            j = seen.get(val, None)
            
            if j is not None and i - j <= k:
                return True

            seen[val] = i
            


        return False



        