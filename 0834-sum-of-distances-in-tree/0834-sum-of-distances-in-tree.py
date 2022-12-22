class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.adj, self.n = defaultdict(set), n
        for i, j in edges:
            self.adj[i].add(j), self.adj[j].add(i)
        self.count, self.res = {i:1 for i in range(n)}, [0] * n
        self.dfs_subtree_size(0)
        self.dfs_distance(0)
        return self.res

    def dfs_subtree_size(self, node, pre=-1):
        for i in self.adj[node]:
            if i != pre:
                self.dfs_subtree_size(i, node)
                self.count[node] += self.count[i]
                self.res[node] += self.res[i] + self.count[i]
    def dfs_distance(self, node, pre=-1):
        for i in self.adj[node]:
            if i != pre:
                self.res[i] = self.res[node] - self.count[i] + self.n - self.count[i]
                self.dfs_distance(i, node)

            
        