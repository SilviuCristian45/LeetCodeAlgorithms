# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = 0
        result = None

        def reverseList(head: ListNode) -> ListNode:
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

        while l1 or l2:
            left, right = 0, 0
            if l1:
                left = l1.val
            if l2:
                right = l2.val                
            computation = (left + right + temp)
            newVal = computation % 10
            temp = computation // 10
            newNode = ListNode(newVal)
            if not result:
                result = newNode
            else:
                newNode.next = result
                result = newNode
            l1 = l1.next
            l2 = l2.next
        
        if temp != 0:
            newNode = ListNode(temp)
            newNode.next = result
            result = newNode

        return reverseList(result)



s = Solution()
s.addTwoNumbers()