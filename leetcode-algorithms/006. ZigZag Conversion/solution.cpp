#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {

    	if(s=="" || numRows==1)
    		return s;

    	string ss="";

    	string res[100];

    	int row=0,delta = 1;

    	for(int i=0;i<s.size();i++){
    		res[row] += s[i];
    		row += delta;
    		if(row >= numRows){
    			row = numRows - 2;
    			delta = -1;
    		}
    		if(row < 0){
    			row = 1;
    			delta = 1;
    		}
    	}

    	for(int i=0;i<numRows;i++){
    		ss += res[i];
    	}

    	return ss;
    }
};

int main()
{
	string s("PAYPALISHIRING");
	Solution ss;
	string res = ss.convert(s,3);
	cout<<res<<endl;
}