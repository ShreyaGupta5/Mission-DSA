from collections import defaultdict
from typing import Optional, List

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []

        # DFS function
        def dfs(node, row, col):
            if not node:
                return

            # store (column, row, value)
            nodes.append((col, row, node.val))

            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        # start DFS
        dfs(root, 0, 0)

        # sort by column, then row, then value
        nodes.sort()

        result = defaultdict(list)

        # group by column
        for col, row, value in nodes:
            result[col].append(value)

        return list(result.values())
