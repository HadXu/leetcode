#include <iostream>
#include <string>
using namespace std;


int myAtoi(string str)
{
	long long ans = 0;
	const int maxint = 0x7fffffff;
	const int minint = 0x80000000;
	const long long max = 0x100000000;

	bool flag = false;

	int st = 0;

	while(st<str.length() && str[st]==' ')
		st++;
	if(st<str.length() && str[st]=='+')
		st++;
	else
	{
		if(st<str.length() && str[st]='-')
			flag = true,st++;
	}

	for(int i=st;i<str.length();i++)
	{
		if(str[i]<='9' && str[i]>='0')
		{
			ans = ans*10+str[i]-'0';
			if(ans>max)
				ans = max;
		}
		else
			break;
	}

	if(flag)
		ans = -ans;
	if(ans<minint)
		ans = minint;
	if(ans>maxint)
		ans = maxint;

	return ans;

}
int main()
{
	return 0;
}