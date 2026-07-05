class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:  
        count = Counter(tasks)
        pq = [-val for val in count.values()]
        heapq.heapify(pq)
        time = 0
        q = deque()

        while pq or q:
            # assuming that that whatever is in the heap is > 0 
            time += 1
            
            if not pq:
                time = q[0][1]
            else:
                tasks_remaining = 1 + heapq.heappop(pq) # because the values are inverted! Cannot forget that
                if abs(tasks_remaining) > 0:
                    q.append([tasks_remaining, time + n])
            if q and q[0][1] == time:
                heapq.heappush(pq, q.popleft()[0])
                

   
        return time
            


            






