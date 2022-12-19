class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.adj = defaultdict(lambda: [])
        self.visited = {i: False for i in range(n)}
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)
        return self.dfs(source, destination)
    
    def dfs(self, node, target):
        if node == target: return True
        self.visited[node] = True
        for v in self.adj[node]:
            if not self.visited[v]:
                self.visited[v] = True
                if self.dfs(v, target): return True
        return False