#include <iostream>
#include <set>
#include <math.h>

using namespace std;


bool judgeSquareSum(int c) {
	set<int> s;
	for(int i=0;i<=int(sqrt(c));i++){
		s.insert(i*i);
		if(s.find(c-i*i)!=s.end())
			return true;
	}
	return false;
}

int main()
{
	int c = 10000;
	cout<<judgeSquareSum(c)<<endl;
	return 0;
}