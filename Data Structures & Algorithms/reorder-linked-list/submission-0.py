# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next    # slow is the middle point of the linked list
            fast = fast.next.next

        # cut the second list, make the first list tail null
        second_head = slow.next
        slow.next = None

        # reverse the second list
        prev = None
        curNode = second_head
        while curNode:
            nextNode = curNode.next
            curNode.next = prev
            prev = curNode
            curNode = nextNode
        
        second = prev

        while second:
            tmp1 = head.next
            tmp2 = second.next

            head.next = second
            second.next = tmp1

            head = tmp1
            second = tmp2
