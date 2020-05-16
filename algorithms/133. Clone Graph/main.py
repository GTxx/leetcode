# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        map = {}
        not_visit: set = {node}
        while not_visit:
            newly_not_visit: set = set()
            for node1 in not_visit:
                print(node1.val)
                clone_node = Node(node1.val)
                map[node1] = clone_node
                for neighbor in node1.neighbors:
                    if neighbor not in map:
                        newly_not_visit.add(neighbor)

            not_visit = newly_not_visit

        visited: set = set()
        not_visit = {node}
        while not_visit:
            newly_not_visit: set = set()
            for node1 in not_visit:
                visited.add(node1)
                print(node1.val)
                clone_node = map.get(node1)
                neighbors = []
                for neighbor in node1.neighbors:
                    neighbors.append(map.get(neighbor))
                    if neighbor not in visited:
                        newly_not_visit.add(neighbor)
                clone_node.neighbors = neighbors
            not_visit = newly_not_visit
        return map.get(node)


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2, n3]
    n2.neighbors = [n1, n4]
    n3.neighbors = [n1, n4]
    n4.neighbors = [n2, n3]
    s = Solution()
    node_new = s.cloneGraph(n1)
    assert node_new.val == 1
    assert set([n.val for n in node_new.neighbors]) == {2, 3}
    assert set([n.val for n in node_new.neighbors]) == {2, 3}
