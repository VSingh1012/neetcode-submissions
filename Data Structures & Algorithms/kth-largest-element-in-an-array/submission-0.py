class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
            pq = nums
            heapq.heapify(pq) # O(nlog(n))

            while len(pq) > k:
                heapq.heappop(pq)

            return pq[0]

