class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for o in range(len(nums)):
                if (x != o):
                    if (nums[x] + nums[o] == target):
                        return [x, o]
            
        