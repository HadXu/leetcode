#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string longestCommonPrefix(vector<string>& strs) {
    if(strs.size() == 0)
    	return "";

    sort(strs.begin(),strs.end());
    string res = "";

    int len = min(strs[0].size(),strs[strs.size()-1].size());

    for(int i=0;i<len;i++){
    	if(strs[0][i] != strs[strs.size()-1][i])
    		break;
    	res += strs[0][i];
    }
    return res;
}

int main()
{
	vector<string> strs{};
	string res = longestCommonPrefix(strs);
	cout<<res<<endl;
	return 0;
}