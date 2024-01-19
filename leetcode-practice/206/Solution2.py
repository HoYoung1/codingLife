# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head

        prev = head
        current = head
        while current.next is not None:
            forward = current.next
            current.next = prev
            prev = current
            current = forward

        return prev


def printNodes(head):
    current_node = head

    while current_node.next is not None:
        print(current_node.val)
        current_node = current_node.next


Solution().reverseList(head=ListNode(val=1, next=ListNode(val=2)))
Solution().reverseList(head=ListNode(val=1))



