# Definition for singly-linked list.
from unittest import result


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        resultListHead = None

        def appendStart(newValue: int):
            newNode = ListNode(newValue)
            if not resultListHead:
                resultListHead = newNode
                return
            newNode.next = resultListHead
            resultListHead = newNode

        while head:
            appendStart(head.val)
            head = head.next
        
        return resultListHead

s = Solution()
head = ListNode()
res = s.reverseList()
while res:
    print(res.val)
    res = res.next
