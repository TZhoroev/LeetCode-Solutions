class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Find either graph contains cycle or not.
        # Initialize all nodes are not visited
        self.visited = [False for _ in range(numCourses)]
        # store adjacency list
        self.adj = defaultdict(lambda: [])
        for a, b in prerequisites:
            self.adj[b].append(a)
        for node in range(numCourses):
            if self.dfs(node): return False
        return True
        
    
    def dfs(self, node):
        if self.visited[node]: return True
        self.visited[node] = True
        for v in self.adj[node]:
            if self.dfs(v): return True
        self.adj[node] = []
        self.visited[node] = False
        return False
        
        