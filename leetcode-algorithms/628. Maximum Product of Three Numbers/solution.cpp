#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maximumProduct(vector<int>& nums) {
	sort(nums.begin(), nums.end());
	int len = nums.size();

	return max(nums[0]*nums[1]*nums[len-1],nums[len-1]*nums[len-2]*nums[len-3]);

}

int main()
{
	vector<int> s{-4,-3,-2,-1,60};

	int res = maximumProduct(s);

	cout<<res<<endl;

	return 0;
}