class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        outcomes = {}
        for match in matches:
            if match[0] not in outcomes: outcomes[match[0]] = 0
            if match[1] not in outcomes: outcomes[match[1]] = 0   
            outcomes[match[1]] += 1
        a, b = [], []
        for player, looses in outcomes.items():
            if looses == 0:
                a.append(player)
            elif looses == 1:
                b.append(player)
        a.sort()
        b.sort()
        return [a, b]
        