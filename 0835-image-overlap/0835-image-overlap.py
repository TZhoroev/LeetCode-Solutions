from collections import defaultdict
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        I_1, I_2, d = [], [] , defaultdict(lambda:0)
        for r in range(len(img1)):
            for c in range(len(img1[0])):
                if img1[r][c]: I_1.append((r, c))
                if img2[r][c]: I_2.append((r, c))
        for r_1, c_1 in I_1:
            for r_2, c_2 in I_2:
                d[(r_2-r_1, c_2 - c_1)] += 1
        return max(d.values()) if d.values() else 0
        