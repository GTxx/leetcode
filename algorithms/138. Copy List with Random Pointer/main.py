# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        map = {}
        current = head
        while current:
            new_node = Node(current.val)
            map[current] = new_node
            current = current.next
        current = head
        while current:
            next = current.next
            random = current.random
            new_node = map.get(current)
            new_node.next = map.get(next, None)
            new_node.random = map.get(random, None)
            current = current.next
        return map.get(head, None)


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n1.next = n2
    n1.random = n2
    n2.random = n2
    s = Solution()
    newNode1 = s.copyRandomList(n1)
    newNode2 = newNode1.next
    assert newNode1.val == 1
    assert newNode2.val == 2
    assert newNode1.next is newNode2
    assert newNode2.random is newNode2
    assert newNode1.random is newNode2


