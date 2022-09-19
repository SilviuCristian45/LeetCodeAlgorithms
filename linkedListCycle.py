# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, NextNode=None):
        self.val = x
        self.next = NextNode

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # dictionary = set()
        # while head:
        #     print(head)
        #     if head in dictionary:
        #         return True
        #     dictionary.add(head)
        #     head = head.next
        # return False
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

s = Solution()
a = ListNode(-4)
b = ListNode(0, a)
a.next = b
c = ListNode(2, b)
d = ListNode(3, c)
res = s.hasCycle(d)
print(res)