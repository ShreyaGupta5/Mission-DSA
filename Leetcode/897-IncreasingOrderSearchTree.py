class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = TreeNode()
        k = dummy
        stack = []

        while stack or root:

            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
                
            k.right = root
            root.left = None
            k = root

            root = root.right

        return dummy.right
