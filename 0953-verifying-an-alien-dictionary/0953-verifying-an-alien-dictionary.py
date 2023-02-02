class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {s: index for index, s in enumerate(order)}
        prev = []
        for i in range(len(words)):
            current = [d[s] for s in words[i]]
            if current < prev:
                return False
            prev = current
        return True
        