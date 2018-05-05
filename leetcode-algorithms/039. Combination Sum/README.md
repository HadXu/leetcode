# 这是一道非常有意思的题目

使用递归方式来做


```cpp
void dfs(vector<int>& nums, int target, int index, vector<int> & path, vector<vector<int>> &res){
    if(target<0){
        return;
    }
    if(target==0){
        res.push_back(path);
        return;
    }
    for(int i=index; i<nums.size();i++){
        path.push_back(nums[i]);
        dfs(nums, target-nums[i], i, path, res);
        path.pop_back();
    }
        
}

vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    vector<vector<int>> res;
    vector<int> path;
    sort(candidates.begin(), candidates.end());
    dfs(candidates, target, 0, path, res);
    return res;
}
```

