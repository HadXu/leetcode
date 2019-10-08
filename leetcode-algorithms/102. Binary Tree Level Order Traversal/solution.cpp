class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<TreeNode*> q;
	if(root){
		q.push(root);
	}
	vector<int> inner;
	vector<vector<int> > outer;
	TreeNode *node;
	while(!q.empty()){
		int size = q.size();
		inner.clear();
		while(size-->0){
			node = q.front();
			q.pop();
			inner.push_back(node->val);
			if(node->left)
				q.push(node->left);
			if(node->right)
				q.push(node->right);
		}
		outer.push_back(inner);
	}
	return outer;
    }
};