from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(lambda:[])
        for word in strs:
            d["".join(sorted(word))].append(word)
        return [x for x in d.values()]
       