# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next

from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_size = 1
        current_node = head

        # get list_size
        while current_node.next is not None:
            list_size += 1
            current_node = current_node.next

        #
        if list_size == n:
            head = None
        else:
            current_node = head
            for i in range(list_size-n-1):
                current_node = current_node.next
            current_node.next = current_node.next.next
        printNodes(head)

def printNodes(head):
    current_node = head

    while current_node.next is not None:
        print(current_node.val)
        current_node = current_node.next





Solution().removeNthFromEnd(head=ListNode(val=1, next=ListNode(val=2)), n=1)
Solution().removeNthFromEnd(head=ListNode(val=1), n=1)

