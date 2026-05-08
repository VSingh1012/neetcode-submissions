class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = defaultdict(int) # default dictionary with 0s as values

         # nums and their counts
        counts = []
        res = []

        for num in nums:
            nums_dict[num] += 1

        # Now we have unique nums with counts,
        for key in nums_dict.keys():
            counts.append([nums_dict[key], key])
        
        counts.sort()

        for it in range(k):
            pair = counts[(len(counts) - 1) - it]
            res.append(pair[1])


        return res

        # should have [1, 2, 3] for first test case


            
    






