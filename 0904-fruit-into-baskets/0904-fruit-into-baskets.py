class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left,  d, count = 0, dict(), 0
        ans = 0
        for fruit in fruits:
            if fruit in d:
                d[fruit] += 1
            else:
                d[fruit] = 1
                while len(d) > 2:
                    d[fruits[left]] -= 1
                    if not d[fruits[left]]:
                        del d[fruits[left]]
                    left += 1
                    count -= 1
            count += 1
            ans = max(ans, count)
        return max(ans, count)
                
        