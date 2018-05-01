class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for(int v:nums)
            res ^= v;
        return res;
    }
};