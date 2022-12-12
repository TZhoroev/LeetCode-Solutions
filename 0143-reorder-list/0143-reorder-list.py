# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # reverse right half
        slow = self.reverseLinkedlist(slow)
        left = head
        while slow.next:
            f, s = left.next, slow.next
            left.next = slow
            slow.next = f
            left, slow = f, s



    def reverseLinkedlist(self, head):
            c_node = head
            prev_node = None
            next_node = head
            while c_node:
                next_node = c_node.next
                c_node.next = prev_node
                prev_node = c_node
                c_node = next_node
            return prev_node


