class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for x in range(len(nums)):
            count = 0
            duplicate = nums[x]
            for y in range(len(nums)):
                if (duplicate == nums[y]):
                    count += 1
            if (count > 1):
                return True

        return False
         