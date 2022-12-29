class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans, heap, current_time, i = [], [], 0, 0
        tasks[:] = [(e, p, i) for i, (e, p) in enumerate(tasks)]
        tasks.sort()
        print(tasks)
        while len(ans) != len(tasks):
            if not heap and current_time < tasks[i][0] :
                current_time = tasks[i][0]
            while i < len(tasks) and current_time >= tasks[i][0]:
                heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            task = heappop(heap)
            current_time += task[0]
            ans.append(task[1])
        return ans
            