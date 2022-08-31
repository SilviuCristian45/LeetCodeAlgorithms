# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cloneHead = head
        count = 0
        while cloneHead != None:
            count += 1
            cloneHead = cloneHead.next
        index = 0
        cloneHeadResult = head

        if count == 1:
            return None
        if count == n:
            return head.next

        while head != None:
            if index == count - n - 1: #if we are at n node near the end then we delete
                head.next = head.next.next
            index += 1
            head = head.next
        return cloneHeadResult

s = Solution()
a = ListNode(1)
b = ListNode(2, a)
c = ListNode(3, b)
d = ListNode(4, c)

def printList(head):
    while head != None:
        print(head.val, end=" ")
        head = head.next

result = s.removeNthFromEnd(a, 1)
printList(result)