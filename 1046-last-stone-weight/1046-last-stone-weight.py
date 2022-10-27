from sortedcontainers import SortedList
class Solution:
    def lastStoneWeight(self, A: List[int]) -> int:
        A = SortedList(A)
        while len(A) > 1:
            a = A.pop()
            b = A.pop()
            if a!=b:
                A.add(a-b)
        return A[0] if A else 0
        