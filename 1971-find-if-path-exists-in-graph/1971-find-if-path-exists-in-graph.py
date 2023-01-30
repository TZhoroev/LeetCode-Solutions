class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.adj = defaultdict(lambda: [])
        self.visited = {i: False for i in range(n)}
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)
        return self.bfs(source, destination)
    
    def bfs(self, node, target):
        Q = deque()
        Q.append(node)
        self.visited[node] = True
        while Q:
            node = Q.popleft()
            if node == target: return True
            for v in self.adj[node]:
                if not self.visited[v]:
                    self.visited[v] = True
                    Q.append(v)
        return False

    def dfs(self, node, target):
        if node == target: return True
        self.visited[node] = True
        for v in self.adj[node]:
            if not self.visited[v]:
                self.visited[v] = True
                if self.dfs(v, target): return True
        return False