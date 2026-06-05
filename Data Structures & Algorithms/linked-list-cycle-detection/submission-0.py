# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        nextNode = head
        while nextNode:
            if nextNode in seen:
                return True
            else:
                seen.add(nextNode)
                nextNode = nextNode.next
        return False