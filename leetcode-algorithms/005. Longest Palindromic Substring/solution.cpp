#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
	int maxLen = 0, lo = 0;
public:
    string longestPalindrome(string s) {
        int len = s.length();
        if(len<2)
        	return s;
        for(int i=0;i<len-1;i++){
        	f(s,i,i);
        	f(s,i,i+1);
        }
        return s.substr(lo,maxLen);
    }

private:
	void f(string s,int j,int k){
		while(j>=0 && k<s.length() && s[j]==s[k]){
			j--;
			k++;
		}
		if(maxLen<k-j-1){
			lo = j+1;
			maxLen = k-j-1;
		}
	}

};

int main()
{
	string s("cbbd");
	Solution so;
	string res = so.longestPalindrome(s);
	cout<<res<<endl;
}