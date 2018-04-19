#include <iostream>
#include <vector>

using namespace std;


int searchInsert(vector<int>& nums, int target) {
	 int res = 0;
	 for(auto v:nums)
	 {
	 	if(v<target)
	 		res++;
	 }    
	 return res;
}

int main()
{
	vector<int> nums={1,3,5,6};
	int target = 0;
	int res = searchInsert(nums, target);
	cout<<res<<endl;
	return 0;
}