from collections import defaultdict
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = defaultdict(lambda:False)
        prev = ListNode()
        curr_node = head
        while curr_node:
            if not d[curr_node.val]: 
                d[curr_node.val]=True
                prev, curr_node = curr_node, curr_node.next
            else: 
                prev.next = curr_node.next
                curr_node = curr_node.next
        return head