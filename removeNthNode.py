# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        left, right = head, head
        for _ in range(0, n):
            right = right.next
        if right.next:
            while right.next:
                left = right
                for _ in range(0, n):
                    right = right.next
            #print(left.val)
            left.next = left.next.next
            return head
        left.next = right
        return left

s = Solution()

d = ListNode(5)
c = ListNode(4, d)
b = ListNode(3, c)
a = ListNode(2, b)
head = ListNode(1, a)

res = s.removeNthFromEnd(head, 2)
while res:
    print(res.val)
    res = res.next