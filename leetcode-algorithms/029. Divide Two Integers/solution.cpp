#include <iostream>
using namespace std;
int divide(int dividend, int divisor) {
	if(divisor==0 || (dividend == INT_MIN && divisor==-1))
		return INT_MAX;

	int sign = ((divisor<0)^(dividend<0))?-1:1;
	long long dvd = labs(dividend);
	long long dvs = labs(divisor);
	int res = 0;
	while(dvd>=dvs)
	{
		long long tmp = dvs;
		int mulpiple = 1;
		while(dvd>=(tmp<<1))
		{
			tmp <<= 1;
			mulpiple <<= 1;
		}
		dvd -= tmp;
		res += mulpiple;
	}
	return sign==1?res:-res;
}
int main()
{
	int dividend = 15, divisor = 3;
	int res = divide(dividend,divisor);
	cout<<res<<endl;

	cout<<INT_MAX<<INT_MIN<<endl;

	return 0;
}