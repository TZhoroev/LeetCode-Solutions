class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(lambda: defaultdict(lambda: False))
        deg = defaultdict(lambda:0)
        for a, b in edges:
            adj[a][b] = True
            deg[a] += 1
            adj[b][a] = True
            deg[b] += 1
        odd = 0
        odd_vertices = []
        for node in range(1, n + 1):
            if deg[node] % 2:
                odd +=1
                odd_vertices.append(node)
        if odd == 0: return True
        elif odd == 2:
            a = odd_vertices[0]
            b = odd_vertices[1]
            if not adj[a][b]:
                return True
            for c in range(1, n + 1):
                if c != a and c != b:
                    if not adj[a][c] and not adj[b][c]:
                        return True
        elif odd == 4:
            a = odd_vertices[0]
            b = odd_vertices[1]
            c = odd_vertices[2]
            d = odd_vertices[3]
            if not adj[a][b] and not adj[c][d]:
                return True
            elif not adj[a][c] and not adj[b][d]:
                return True
            elif not adj[a][d] and not adj[b][c]:
                return True
            
        else:
            return False
                
                
        