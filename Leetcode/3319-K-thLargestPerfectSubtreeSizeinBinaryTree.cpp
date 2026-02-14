class Solution {
public:
    int kthLargestPerfectSubtree(TreeNode* root, int k) {
        vector<int> perfectSizes;
        dfs(root, perfectSizes);
        if ((int)perfectSizes.size() < k) {
            return -1;
        }
        // sort descending
        sort(perfectSizes.begin(), perfectSizes.end(), greater<int>());
        return perfectSizes[k - 1];
    }

private:
    // Returns: pair {isPerfect, sizeOfSubtreeIfPerfectElseUndefined}
    pair<bool,int> dfs(TreeNode* node, vector<int>& perfectSizes) {
        if (node == nullptr) {
            // empty tree is considered perfect with size 0
            return {true, 0};
        }
        auto leftRes = dfs(node->left, perfectSizes);
        auto rightRes = dfs(node->right, perfectSizes);

        bool leftPerfect = leftRes.first;
        bool rightPerfect = rightRes.first;
        int leftSize = leftRes.second;
        int rightSize = rightRes.second;

        if (leftPerfect && rightPerfect && leftSize == rightSize) {
            int currSize = leftSize + rightSize + 1;
            perfectSizes.push_back(currSize);
            return {true, currSize};
        } else {
            return {false, 0};
        }
    }
};
