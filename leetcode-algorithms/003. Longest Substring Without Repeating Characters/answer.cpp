#include <iostream>
#include <algorithm>
#include <string>
#include <map>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res = 0;
        map<char,int> m;
        for(auto i=0,j=0; i<s.size(); i++){
        	if (m.find(s[i]) != m.end())
        		j = max(j,m[s[i]]+1);
        	m[s[i]] = i;
        	res = max(res,i-j+1);
        }
        return res;
    }
};

int main()
{
	string s("abcdabcde");
	Solution solution;
	int res = solution.lengthOfLongestSubstring(s);
	cout<<res<<endl;
	return 0;
}