# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        res = None

        def appendFinal(newVal):
            nonlocal res
            newNode = ListNode(newVal)
            if not res:
                res = newNode
                return
            clone = res
            while clone.next:
                clone = clone.next
            clone.next = newNode 

        def printList(x: ListNode):
            while x:
                print(x.val)
                x = x.next
        
        #driver
        while list1 and list2:
            if list1.val <= list2.val:
                appendFinal(list1.val)
                list1 = list1.next
                continue
            appendFinal(list2.val)
            list2 = list2.next
        
        while list1: appendFinal(list1.val); list1 = list1.next
        while list2: appendFinal(list2.val); list2 = list2.next

        #printList(x=res)
        return res

s = Solution()

h3 = ListNode(4)
h2 = ListNode(2, h3)
h1 = ListNode(1, h2)

g3 = ListNode(4)
g2 = ListNode(3, g3)
g1 = ListNode(1, g2)

s.mergeTwoLists(h1, g1)





