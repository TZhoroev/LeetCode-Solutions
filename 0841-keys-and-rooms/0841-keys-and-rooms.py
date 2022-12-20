class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        seen = set()
        def dfs(node):
            seen.add(node)
            for v in rooms[node]:
                if v not in seen:
                    dfs(v)

        dfs(0)
        return len(seen)==n