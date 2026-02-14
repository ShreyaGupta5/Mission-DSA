class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_s = float('-inf')
        def f(node):
            nonlocal max_s
            if not node:
                return 0
            
            left = max(f(node.left),0)
            right = max(f(node.right),0)
            Total = node.val + left + right
            max_s = max(max_s, Total)
            return node.val + max(left, right)
        f(root)
        return max_s
