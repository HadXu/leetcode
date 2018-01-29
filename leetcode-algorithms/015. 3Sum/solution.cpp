#include <iostream>
#include <vector>
using namespace std;

vector<vector<int> > threeSum(vector<int>& nums) {
	if(nums.size() <=2) return {};
	vector<vector<int> > ans;
	sort(nums.begin(), nums.end());
	for(int i=0;i<nums.size()-2;i++)
	{
		if(i==0 || (i>0 && nums[i]!=nums[i-1]))
		{
			int lo = i+1,hi = nums.size()-1,sum = -nums[i];
			while(lo<hi)
			{
				if(nums[lo]+nums[hi]==sum)
				{
					vector<int> tmp;
					tmp.push_back(nums[i]);
					tmp.push_back(nums[lo]);
					tmp.push_back(nums[hi]);
					ans.push_back(tmp);
					while(lo<hi && nums[lo]==nums[lo+1]) lo++;
					while(lo<hi && nums[hi]==nums[hi-1]) hi--;
					lo++,hi--;
				}
				else if(nums[lo]+nums[hi]<sum)
					lo++;
				else
					hi--;
			}
		}
	}
	return ans;
}

int main()
{
	vector<int> nums{-4,-1,-1,0,1,2};
	vector<vector<int> > ans = threeSum(nums);
	cout<<ans.size()<<endl;
	return 0;
}