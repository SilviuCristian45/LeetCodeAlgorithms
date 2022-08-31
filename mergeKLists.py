from logging.config import valid_ident
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def appendLinkedList(self, newNode):
        if not self:
            self = newNode  
        clone = self
        while clone.next != None:
            clone = clone.next
        clone.next = newNode
    def printList(self):
        clone = self
        while clone != None:
            print(clone.val, end=" ")
            clone = clone.next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        pass




def merge2List(headA: ListNode, headB: ListNode):
    result = None
    while headA.next and headB.next:
        if headA.val > headB.val:
            newNode = ListNode(headB.val)
            appendLinkedList(result, newNode)
        elif headA.val <= headB.val:
            newNode =  ListNode(headA.val)
            appendLinkedList(result, newNode)
            


s = Solution()

# res = ListNode(123)
# res.appendLinkedList( ListNode(23))
# res.appendLinkedList( ListNode(15))
# res.appendLinkedList( ListNode(999))
# res.printList()