class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [[(math.dist(points[x], [0,0]) * -1), x] for x in range(len(points))]

        heapq.heapify(distances)

        while len(distances) > k:
            heapq.heappop(distances)

        # for the bottom three distances
        res = []
        while distances:
            i = heapq.heappop(distances)[1]
            res.append(points[i])

        return res

    