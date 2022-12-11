# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        heap = []
        for index in range(k):
            if lists[index]:
                heap.append((lists[index].val, index))
                lists[index] = lists[index].next
        dummy_head = ListNode()
        res = dummy_head
        heapify(heap)
        while heap:
            val, index = heappop(heap)
            dummy_head.next = ListNode(val)
            dummy_head = dummy_head.next
            if lists[index]:
                heappush(heap, (lists[index].val, index))
                lists[index] = lists[index].next
        return res.next