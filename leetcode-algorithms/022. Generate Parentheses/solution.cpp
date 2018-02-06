#include <iostream>
#include <vector>
#include <string>
using namespace std;


void DFS(int left, int right, string out, vector<string> &res)
{
	if(left>right)
		return;
	if(left==0 && right==0)
		res.push_back(out);
	else
	{
		if(left>0)
		{
			DFS(left-1,right,out+"(",res);
		}
		if(right>0)
		{
			DFS(left,right-1,out+")",res);
		}
	}
}

vector<string> generateParenthesis(int n) {
	vector<string> res;
	DFS(n,n,"",res);
	return res;
}

int main()
{
	int n=3;
	vector<string> res = generateParenthesis(n);
	cout<<res.size()<<endl;
	return 0;
}