class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        deg = [0 for _ in range(n)]
        for a, b in prerequisites:
            adj[b].append(a)
            deg[a] += 1
        Q = [x for x, val in enumerate(deg) if val == 0]
        Q = deque(Q)
        ans, count = [0 for _ in range(n)], 0
        while Q:
            node = Q.popleft()
            ans[count] = node
            for v in adj[node]:
                deg[v] -= 1
                if deg[v] == 0:
                    Q.append(v)
            count += 1
        return ans if count == n else []
            
        
        