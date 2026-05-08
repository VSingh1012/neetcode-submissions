class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic = defaultdict(int)
        numsList = []
        res = []

        for num in nums:
            dic[num] += 1 # Counts for the numeric values stored in a dictionary


        for key in dic.keys():
            numsList.append([dic[key], key])

        numsList.sort()

        for i in range(k):
            pair = numsList[(len(numsList) - 1) - i]
            res.append(pair[1])

        return res


        