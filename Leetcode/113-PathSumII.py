#DFS
class Solution:
    def pathSum(self, root, targetSum):
        res = []
        
        def dfs(node, path, total):
            if not node:
                return
            
            path.append(node.val)
            total += node.val
            
            if not node.left and not node.right and total == targetSum:
                res.append(path[:])
            
            dfs(node.left, path, total)
            dfs(node.right, path, total)
            
            path.pop()
        
        dfs(root, [], 0)
        return res

#BFS
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return[]
        M = []
        Q = [(root, [], targetSum)]
        while Q:
            node, path, k = Q.pop(0)
            path.append(node.val)
            k = k - node.val 
            if not node.left and not node.right and k==0:
                M.append(path)
            if node.left:
                Q.append((node.left, path[:], k))
            if node.right:
                Q.append((node.right, path[:], k))
        return M
