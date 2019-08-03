class Solution {
public:
    bool helper(TreeNode* left,TreeNode* right){
        if(!left && !right) return true;
        if(!left && right || !right && left || left->val != right->val) return false;
        return helper(left->left,right->right) and helper(left->right,right->left);
    }
    bool isSymmetric(TreeNode* root) {
        if(!root) return true;
        return helper(root->left,root->right);
    }
};