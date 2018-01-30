#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>
using namespace std;

int threeSumClosest(vector<int>& nums, int target) {
	if(nums.size()<=3)
		return accumulate(nums.begin(),nums.end(),0);
	sort(nums.begin(), nums.end());

	int ans = nums[0]+nums[1]+nums[2];
	int n = nums.size();

	for (int i = 0; i < n-2; ++i)
	{
		int j=i+1,k=n-1;
		while(j<k)
		{
			int sum = nums[i]+nums[j]+nums[k];
			if(abs(target-ans)>abs(target-sum))
			{
				ans = sum;
				if(ans==target)
					return ans;
			}
			(sum>target)?k--:j++;
		}
	}
	return ans;

}

int main()
{
	std::vector<int> v{-1,2,1,4};
	int res = threeSumClosest(v,1);
	std::cout<<res<<endl;
	return 0;
}
