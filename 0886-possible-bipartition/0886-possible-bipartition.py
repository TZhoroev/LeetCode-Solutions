class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(lambda:[])
        for a, b in dislikes:
            adj[a - 1].append(b - 1)
            adj[b - 1].append(a - 1)
        dist = [float("inf") for _ in range(n)]
        # dist = even --> class 0
        # dist = odd --> class 1
        def bfs(node):
            dist[node] = 0
            Q = deque()
            Q.append(node)
            while Q:
                u = Q.popleft()
                for v in adj[u]:
                    if dist[v] > dist[u] + 1:
                        dist[v] = dist[u] + 1
                        Q.append(v)
                    else:
                        if (dist[v] - dist[u]) % 2 == 0:
                            return False
            return True
        for node in range(n):
            if dist[node] == float("inf"):
                if not bfs(node): return False
        return True
            