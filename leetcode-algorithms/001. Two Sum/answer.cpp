#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
    	map<int,int> m;
    	vector<int> res;
    	for(int i=0;i<nums.size();i++){
    		if( m.find( target-nums[i] ) == m.end()){
    			m[nums[i]] = i;
    		}
    		else{
    			res.push_back(m[target - nums[i]]);
    			res.push_back(i);
    			return res;
    		}
    	}
    	return res;
    }

};

int main(){
	Solution s;
	vector<int> nums{2,7,11,15};
	int target = 9;
	vector<int> res = s.twoSum(nums,target);
	for (std::vector<int>::iterator i = res.begin(); i != res.end(); ++i)
	{
		cout<<*i<<endl;	
	}
	return 0;
}