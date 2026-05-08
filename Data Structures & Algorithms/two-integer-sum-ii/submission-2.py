class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        res = []

        for i, v in enumerate(numbers):
            diff = target - v
                        
            r = len(numbers) - 1

            while (r > i):
                if diff == numbers[r]: 
                    res.append([i + 1, r + 1])

                r -= 1

        return res[0]
    
            




        return res[0]