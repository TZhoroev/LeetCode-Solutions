class Solution:
    def frequencySort(self, s: str) -> str:
        C = Counter(s).most_common()
        res = ""
        for key, val in C:
            res += key*val
        return res


            

        