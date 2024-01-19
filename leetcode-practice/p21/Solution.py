# Definition for singly-linked list.
import sys
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = None

        # 큰거 먼저 선정하자
        current = None
        if list1.val < list2.val:
            current = list2
            list2 = list2.next
        else:
            current = list1
            list1 = list1.next


        while True:
            if list1.next is None:
                current.next = list2
                break
            elif list2.next is None:
                current.next = list1
                break

            if list1.val < list2.val:
                current.next = list1.val
                list1 = list1.next
            else:
                current.next = list2.val
                list2 = list2.next

        printNodes(current)
        return current


def printNodes(head):
    current_node = head

    while current_node.next is not None:
        print(current_node.val)
        current_node = current_node.next

l1 = ListNode(val=1, next=ListNode(val=2))
l2 = ListNode(val=1, next=ListNode(val=2))

Solution().mergeTwoLists(l1, l2)
# Solution().reverseList(head=ListNode(val=1))



