class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        if n == 0: return []
        res = []
        stack = [(0, [0])]
        while stack:
            node, path = stack.pop()
            if node == n - 1:
                res.append(path)
            else:
                for v in graph[node]:
                    stack.append((v, path +[v]))
        return res
        