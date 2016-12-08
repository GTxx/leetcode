class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return [0]
        edge_dict = {}
        for n1, n2 in edges:
            if n1 in edge_dict:
                edge_dict[n1].append(n2)
            else:
                edge_dict[n1] = [n2]

            if n2 in edge_dict:
                edge_dict[n2].append(n1)
            else:
                edge_dict[n2] = [n1]

        def find_deeppest_node(node, parent):
            longest_path = []
            for child in edge_dict[node]:
                if child == parent:
                    continue
                path = find_deeppest_node(child, node)
                if len(path) > len(longest_path):
                    longest_path = path
            return [node] + longest_path

        path = find_deeppest_node(0, None)

        longest_path = find_deeppest_node(path[-1], None)

        length = len(longest_path)
        if length % 2 == 0:
            return [longest_path[(length-2)//2], longest_path[length//2]]
        else:
            return [longest_path[(length-1)//2]]


if __name__ == "__main__":
    s = Solution()
    print(s.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
    print(s.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
    print(s.findMinHeightTrees(1, []))
