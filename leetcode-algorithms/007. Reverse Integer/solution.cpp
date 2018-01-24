#include <iostream>
using namespace std;


int reverse(int x) {
	long long res = 0;
	int flag = 0;
	if(x<0)
		flag = 1;
	x = abs(x);
	while(x)
	{
		res = res*10 + x % 10;
		x /= 10;
	}

	if(flag)
		res = res * -1;
    return (res<INT_MIN || res>INT_MAX) ? 0 : res;
	
    }

int main()
{
	int x = -123;
	cout<<reverse(x)<<endl;
	return 0;
}