class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        adj = defaultdict(lambda: [])
        n = len(rooms)
        for room, keys in enumerate(rooms):
            adj[room].extend(keys)
        seen = set()
        def dfs(node):
            seen.add(node)
            for v in adj[node]:
                if v not in seen:
                    dfs(v)

        dfs(0)
        return len(seen)==n