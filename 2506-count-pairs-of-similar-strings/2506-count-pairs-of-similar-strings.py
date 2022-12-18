class Solution:
    def similarPairs(self, words: List[str]) -> int:
        l_sets = []
        for word in words:
            l_sets.append(set([*word]))
        print(l_sets)
        count = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if l_sets[i]==l_sets[j]:
                    count +=1
        return count
        