class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        C = Counter(arr)
        occ = set()
        for val in C.values():
            if val in occ: return False
            occ.add(val)
        return True
        
        