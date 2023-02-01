class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        parent, rank, seen, ans = {}, {}, set(), 1
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def join(x, y):
            x_head, y_head = find(x), find(y)
            parent[x_head] = y_head
            rank[y_head] += rank[x_head]
            return rank[y_head]
            
        for num in nums:
            if num in seen:
                continue
            else:
                seen.add(num)
                parent[num], rank[num] = num, 1
                if num +1 in seen:
                    length = join(num, num + 1)
                    ans = max(ans, length)
                if num - 1 in seen:
                    length = join(num - 1, num)
                    ans = max(ans, length)
                
        return ans
                
        

        
        