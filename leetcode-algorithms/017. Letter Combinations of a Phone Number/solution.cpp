#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;
vector<string> letterCombinations(string digits) {
	map<char,string> m;
	m['2'] = "abc";
	m['3'] = "def";
	m['4'] = "ghi";
	m['5'] = "jkl";
	m['6'] = "mno";
	m['7'] = "pqrs";
	m['8'] = "tuv";
	m['9'] = "wxyz";
	vector<string> res;

	if(digits=="")
		return res;
	res.push_back("");
	for(int i=0;i<digits.size();i++)
	{
		vector<string> tempres;
		string chars = m[digits[i]];
		for(int c=0;c<chars.size();c++)
			for(int j=0;j<res.size();j++)
				tempres.push_back(res[j]+chars[c]);
		res = tempres;
	}
	return res;
}

int main()
{
	return 0;
}