#include <iostream>
#include <vector>
using namespace std;

int removeDuplicates(vector<int>& nums) {
	if(nums.size()==0)
		return 0;
	int len = 1;
	for(int i=1;i<nums.size();i++)
	{
		if(nums[i]!=nums[i-1])
			nums[len++] = nums[i];
	}
	return len;
}

int main()
{
	vector<int> nums = {1,1,2};
	int res = removeDuplicates(nums);
	cout<<res<<endl;
	return 0;
}