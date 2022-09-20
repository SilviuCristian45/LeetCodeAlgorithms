
# Definition for a Node.
from pickle import NONE


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        map = { None: None }
        cur = head
        while cur:
            newNodeCopy = Node(cur.val)
            map[cur] = newNodeCopy
            cur = cur.next
        cur = head
        while cur:
            copyNode = map[cur]
            copyNode.next = map[cur.next]
            copyNode.random = map[cur.random]
            cur = cur.next
        return map[head]


s = Solution()
b = Node()
a = Node(4)
res = s.copyRandomList()
        