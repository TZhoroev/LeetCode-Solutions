# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Time-> O(n), Space -> O(n)
        fast, slow = head, head
        # if we have only one element-->True
        if head.next is None: 
            return True
        # store the values of left half
        Q = [] 
        while fast.next and fast.next.next:
            Q.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        # if the array has even number of elements add middle element else skip
        if fast.next:
            Q.append(slow.val)
        slow = slow.next
        # continues until Q is empty or slow.next==None
        while Q:
            c_val = Q.pop()
            if slow.val != c_val: return False
            slow = slow.next
        return True
        