class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        self.adj = defaultdict(lambda: deque())
        indegree = defaultdict(lambda: 0)
        outdegree = defaultdict(lambda: 0)
        for start, end in pairs:
            self.adj[start].append(end)
            outdegree[start] += 1
            indegree[end] += 1
        for node, deg in outdegree.items():
            if deg > indegree[node]:
                start = node
                break

        self.res = deque()
        self.dfs(start)
        return [[self.res[i], self.res[i+1]] for i in range(len(self.res)-1)]


        return pairs
    
    def dfs(self, node):
        while self.adj[node]:
            v = self.adj[node].pop()
            self.dfs(v)
        self.res.appendleft(node)

            

