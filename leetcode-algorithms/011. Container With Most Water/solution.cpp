#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int maxArea(vector<int>& height) {
	int res = 0;
	int i=0,j=height.size()-1;
	while(i<j)
	{
		auto h = min(height[i],height[j]);
		res = max(res,h*(j-i));
		while(height[i]<=h) i++;
		while(height[j]<=h) j--;
	}
	return res;


}
int main()
{
	vector<int> height{7,4,1,100,50};
	int res = maxArea(height);
	cout<<res<<endl;
}