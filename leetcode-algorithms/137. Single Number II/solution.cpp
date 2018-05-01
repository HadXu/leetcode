class Solution {
public:
    int singleNumber(vector<int>& nums) {
        set<int> s(nums.begin(),nums.end());
        size_t a = accumulate(s.begin(),s.end(),0);
        size_t b = accumulate(nums.begin(),nums.end(),0);
        return (3*a-b)/2;
    }
};