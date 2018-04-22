#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int search(vector<int>& nums, int target) {
	int lo = 0, hi = nums.size();

	while(lo<hi){
		int mid = (lo+hi) /2;
		double num = (nums[mid]<nums[0]) == (target<nums[0])
					? nums[mid]
					: target < nums[0]?-INFINITY:INFINITY;
		if(num<target)
			lo = mid + 1;
		else if(num>target)
			hi = mid;
		else
			return mid;
	}
	return -1;
}

int main()
{
	vector<int> nums{4,5,6,7,0,1,2};
	int res = search(nums,2);
	cout<<res<<endl;
}