class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        n = len(nums)

        for i in range(n):
            j = i + 1
            while j < n and (j - i) < k + 1:
                if nums[j] == nums[i]:
                    return True
                j += 1  

        return False



        