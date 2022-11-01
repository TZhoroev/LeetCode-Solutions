# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode()
        val = 0
        prev = dummyhead
        head = head.next
        while head:
            if head.val:
                val += head.val
            else:
                prev.next = ListNode()
                prev = prev.next
                prev.val = val
                val = 0
            head = head.next
        return dummyhead.next
            
        