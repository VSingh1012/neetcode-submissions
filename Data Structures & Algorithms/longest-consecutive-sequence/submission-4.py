class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newNums = set(nums)
        longest_length = 0

        for n in newNums:
            length = 0
            if (n - 1) not in newNums:
                while (n + length) in newNums:
                    length += 1
                longest_length = max(length, longest_length)


        return longest_length