from collections import deque
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        seen = set()
        ans = 0
        queue = deque([start]) 
        while queue:      
            for _ in range(len(queue)):
                word = queue.popleft()          
                if word == end:
                    return ans          
                for i in range(len(word)):
                    for w in ('A', 'C', 'G', 'T'):
                        newWord = word[:i] + w + word[i+1:]             
                        if newWord in bank and newWord not in seen:
                            seen.add(newWord)      
                            queue.append(newWord)
            ans += 1       
        return -1