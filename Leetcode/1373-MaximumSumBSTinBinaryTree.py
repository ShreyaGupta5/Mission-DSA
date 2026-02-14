class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_s = 0

        def f(node):
            if not node:
                return True, float('inf'), float('-inf'), 0

            l_bst, l_min, l_max, l_sum = f(node.left)
            r_bst, r_min, r_max, r_sum = f(node.right)

            # Check BST condition
            if l_bst and r_bst and l_max < node.val < r_min:
                total = l_sum + r_sum + node.val
                self.max_s = max(self.max_s, total)

                return (
                    True,
                    min(l_min, node.val),
                    max(r_max, node.val),
                    total
                )

            # Not a BST
            return False, 0, 0, 0

        f(root)
        return self.max_s
