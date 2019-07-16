#include<vector>
// #include<>
#include<iostream>
#include<queue>
using namespace std;

struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

void show_tree(TreeNode* root){
    queue<TreeNode*> q;
    q.push(root);
    int level = 0;
    while(!q.empty()){
        cout<<"level"<<level<<": ";
        for(int i = q.size()-1;i>=0;i--){
            TreeNode* t = q.front();q.pop();
            if(t->left) q.push(t->left);
            if(t->right) q.push(t->right);
            cout<<t->val<<" ";
            level++;
        }
        cout<<endl;
    }
}

TreeNode* helper(vector<int>& nums,int begin,int end){
    if(begin>end) return NULL;
    int pos = begin;
    for(int i = begin+1;i<=end;i++){
        if(nums[i]>nums[pos]){
            // m = nums[i];
            pos = i;
        }
    }
    // cout<<nums[pos];
    TreeNode* root = new TreeNode(nums[pos]);
    root->left = helper(nums,begin,pos-1);
    root->right = helper(nums,pos+1,end);
    return root;
}

TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
    if(nums.empty()) return NULL;
    return helper(nums,0,nums.size()-1);
}

int main(){
    cout<<"Nums Size: ";
    int k;
    cin>>k;
    vector<int> nums(k);
    for(int i = 0;i<k;i++){
        cin>>nums[i];
    }

    show_tree(constructMaximumBinaryTree(nums));
    return 0;
}