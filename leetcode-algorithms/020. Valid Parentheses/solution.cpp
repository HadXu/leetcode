#include <iostream>
#include <map>
#include <stack>
#include <string>
using namespace std;


bool isValid(string s) {
	stack<char> st;
	map<char,char> m={  {")","("},
						{"}","{"},
						{"]","["}
					}

	for(auto c: s)
	{
		if(c=="["||c=="("||c=="{")
		{
			st.push(c);
			continue;
		}
		if(!st.empty() && m[c]==st.pop())
		{
			st.pop()
		}
		else
			return false;

	}
	return !st.empty();
}

int main()
{
	string s("()");
	bool res = isValid(s);
	cout<<res<<endl;
	return 0;
}