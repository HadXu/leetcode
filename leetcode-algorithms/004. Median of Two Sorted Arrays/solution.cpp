#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if(nums1.size()>nums2.size())
        	return findMedianSortedArrays(nums2, nums1);
        int m = nums1.size(),n=nums2.size();
        int imin=0,imax = m,half_len = (m+n+1) / 2;
        int i = 0,j = 0;
        double max_of_left = 0,min_of_right = 0;
        while(imin<=imax){
        	i = (imin+imax)/2;
        	j = half_len - i;
        	if (i<m && nums2[j-1]>nums1[i])
        		imin = i + 1;
        	else if(i>0 && nums1[i-1]>nums2[j])
        		imax = i - 1;
        	else{
        		if (i==0)
        			max_of_left = nums2[j-1];
        		else if (j==0)
        			max_of_left = nums1[i-1];
        		else
        			max_of_left = max(nums1[i-1],nums2[j-1]);
        		if ((m+n) % 2 == 1)
        			return max_of_left;
        		if (i==m)
        			min_of_right = nums2[j];
        		else if(j==n)
        			min_of_right = nums1[i];
        		else
        			min_of_right = min(nums1[i],nums2[j]);
        		return (min_of_right+max_of_left)/2.;
        	}
        }

    }
};

int main()
{
	Solution s;
	vector<int> v1{1,2};
	vector<int> v2{3,4};

	double res = s.findMedianSortedArrays(v1,v2);
	cout<<res<<endl;

	return 0;
}