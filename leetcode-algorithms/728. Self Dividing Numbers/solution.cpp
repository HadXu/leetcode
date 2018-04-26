#include <iostream>
#include <vector>

using namespace std;

vector<int> selfDividingNumbers(int left, int right) {

	vector<int> res;

	for(int i=left;i<=right;i++){
		int local = i;
		bool flag = true;

		while(local){
			int rem = local % 10;
			local /= 10;
			if(rem==0){
				flag = false;
				break;
			}
			if((i%rem)!=0)
				flag = false;
		}
		if(flag)
			res.push_back(i);

	}
	return res;
}

int main()
{
	int left = 1;
	int right = 22;

	vector<int> res = selfDividingNumbers(left,right);

	for (std::vector<int>::iterator i = res.begin(); i != res.end(); ++i)
	{
		cout<<*i<<endl;	
	}


	return 0;
}