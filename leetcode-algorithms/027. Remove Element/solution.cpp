#include <iostream>
#include <vector>
using namespace std;

int removeElement(vector<int>& nums, int val) {
	int begin = 0;
	for(int i=0;i<nums.size();i++)
	{
		if(nums[i]!=val)
			nums[begin++] = nums[i];
	}
	return begin;
}

int main()
{
	vector<int> nums = {3,2,2,3};
	int res = removeElement(nums,3);
	cout<<res<<endl;
	return 0;
}