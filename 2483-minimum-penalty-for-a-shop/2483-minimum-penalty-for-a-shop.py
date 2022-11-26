class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        max_p = 0
        idx = 0
        cnt = [0, 0]
        for i in range(n):
            if customers[i] == "Y":
                cnt[0] += 1
                cnt[1] = i + 1
            else:
                cnt[0] -= 1
                cnt[1] = i
            if cnt[0] > max_p:
                idx = cnt[1]
            
            max_p = max(max_p, cnt[0])
        return idx
        