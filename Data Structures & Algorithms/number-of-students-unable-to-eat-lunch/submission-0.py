class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        queue = deque(students)

        sandwich_stk = list(reversed(sandwiches)) # reverse for the stack like behavior

        count = 0

        while queue and count < len(queue):
            if queue[0] != sandwich_stk[-1]:
                queue.append(queue.popleft())
                count += 1
            else:
                sandwich_stk.pop()
                queue.popleft()
                count = 0

            

        return len(queue)





        
        