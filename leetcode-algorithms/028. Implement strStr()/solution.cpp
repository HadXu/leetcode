#include <iostream>
#include <string>
using namespace std;

int strStr(string haystack, string needle) {
    for(int i=0;;i++)
    	for(int j=0;;j++)
    	{
    		if(j==needle.size())
    			return i;
    		if(i+j == haystack.size())
    			return -1;
    		if(needle[j]!=haystack[i+j])
    			break;
    	}
}

int main()
{
	string haystack("hello");
	string needle("ll");
	int res = strStr(haystack, needle);
	cout<<res<<endl;
	return 0;
}