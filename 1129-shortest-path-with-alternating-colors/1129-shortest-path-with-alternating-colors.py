class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        edges = defaultdict(lambda: [[], []])
        for a, b in redEdges:
            edges[a][0].append(b)
        for a, b in blueEdges:
            edges[a][1].append(b)
        res = [-1 for _ in range(n)]
        visited = set()
        visited.add((0, 1))
        visited.add((0, 0))
        Q = deque([[0, 0, 0], [0, 1, 0]])
        Q.append((0, 0, 0))
        while Q:
            node, prev, length = Q.popleft()
            res[node] = length if res[node] == -1 else min(length, res[node])
            for v in edges[node][1-prev]:
                if (v, 1 - prev) not in visited:
                    visited.add((v, 1 - prev))
                    Q.append((v, 1 - prev, length + 1))
        return res
        