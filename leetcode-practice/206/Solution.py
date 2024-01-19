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

        def recursive(before_node: ListNode, current_node: ListNode):
            if current_node.next is None:
                # leaf_node
                current_node.next = before_node
                before_node.next = None
            else:
                recursive(current_node, current_node.next)
        recursive(head, head.next)


