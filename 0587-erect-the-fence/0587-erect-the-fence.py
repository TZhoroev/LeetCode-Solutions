class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(a, b, c):
            return (c[1] - b[1]) * (b[0] - a[0]) - (c[0] - b[0]) * (b[1] - a[1])   
        N = len(trees)
        if N == 1:
            return trees
        trees.sort()
        trees = [(x, y) for x, y in trees]           
        # Build lower hull
        lower = []
        for t in trees:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], t) < 0:
                lower.pop()
            lower.append(t)       
        # Build upper hull
        upper = []
        for t in trees:
            while len(upper) >= 2 and cross(upper[-2], upper[-1], t) > 0:
                upper.pop()
            upper.append(t)
            
        return list(set(lower + upper))
        