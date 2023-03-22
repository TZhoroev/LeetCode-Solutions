class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(lambda:[])
        for a, b, d in roads:
            adj[a].append((b, d))
            adj[b].append((a, d))
        Q = deque()
        res = float("inf")
        Q.append(1)
        visited= set()
        while Q:
            node = Q.popleft()
            for v, d in adj[node]:
                res = min(res, d)
                if v not in visited:
                    visited.add(v)
                    Q.append(v)
        return res
                    
        