class Solution {
public:
    TreeNode* increasingBST(TreeNode* root) {
        if (!root) {
            return nullptr;
        }

        TreeNode* dummy = new TreeNode(0);
        TreeNode* current = dummy;

        inorderTraversal(root, current);

        return dummy->right;
    }

private:
    void inorderTraversal(TreeNode* node, TreeNode*& current) {
        if (!node) {
            return;
        }

        inorderTraversal(node->left, current);

        node->left = nullptr;
        current->right = node;
        current = node;

        inorderTraversal(node->right, current);
    }
};
