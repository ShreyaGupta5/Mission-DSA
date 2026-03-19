class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        Q=[(root, targetSum - root.val)]

        while Q:
            node, k = Q.pop(0)
            if not node.left and not node.right and k == 0:
                return True

            if node.left:
                Q.append((node.left,  k - node.left.val))

            if node.right:
                Q.append((node.right, k - node.right.val))

        return False
