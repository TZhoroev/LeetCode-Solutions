class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n -1:
            return -1
        adj = defaultdict(lambda:[])
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)
        visited = set()
        def dfs(node):
            for v in adj[node]:
                if v not in visited:
                    visited.add(v)
                    dfs(v)
        res = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1
        return res - 1 
        