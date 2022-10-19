from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        return sorted(c, key = lambda y: (-c[y], y))[:k]
        