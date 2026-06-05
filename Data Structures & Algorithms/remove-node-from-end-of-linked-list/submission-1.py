# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        
        remove_idx = len(nodes)-n

        if remove_idx == 0:
            head = head.next
            return head

        nodes[remove_idx - 1].next = nodes[remove_idx].next

        return head