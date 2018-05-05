class Solution {
private:
    void dfs(vector<int>& nums, int target, int index, vector<int>& path, vector<vector<int>> &res){
    if(target<0){
        return;
    }
    if(target==0){
        res.push_back(path);
        return;
    }
    for(int i=index; i<nums.size();i++){
        if(i>index && nums[i]==nums[i-1])
            continue;
        path.push_back(nums[i]);
        dfs(nums, target-nums[i], i+1, path, res);
        path.pop_back();
    }

}
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
    vector<int> path;
    sort(candidates.begin(), candidates.end());
    dfs(candidates, target, 0, path, res);
    return res;
    }
};