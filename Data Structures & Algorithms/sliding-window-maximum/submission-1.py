class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [] 
        n = len(nums)
        hp = []

        for x in range(k):
            heapq.heappush(hp, (nums[x] * -1, x))
        res.append(hp[0][0] * -1)

        for i in range(k, n):
            j = i - k + 1        
            while hp and j > hp[0][1]:
                heapq.heappop(hp)

            heapq.heappush(hp, (nums[i] * -1, i)) 
            res.append(hp[0][0] * -1)

        return res

                

    

        

