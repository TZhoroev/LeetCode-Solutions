class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        edges.sort(key=lambda x: max(vals[x[0]], vals[x[1]]))
        n = len(vals)
        par, rank = [i for i in range(n)], [1] * n
        
        def find(p): #find parent of node i
            while par[p] != p:
                par[p]= par[par[p]]
                p = par[p]
            return p
        
        goodPaths = n   
        for a,b in edges:
            parent_a, parent_b = find(a), find(b)
            if vals[parent_a] == vals[parent_b]:
                goodPaths += rank[parent_a] * rank[parent_b]
                par[parent_a] = parent_b
                rank[parent_b] += rank[parent_a]
            elif vals[parent_a] > vals[parent_b]: 
                par[parent_b] = parent_a
            else: 
                par[parent_a] = parent_b
                
        return goodPaths