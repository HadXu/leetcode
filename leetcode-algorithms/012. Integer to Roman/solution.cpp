#include <iostream>
#include <string>
#include <chrono>
using namespace std;
using namespace chrono;



string intToRoman(int num) {
	const int values[] = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
	const string symbols[] = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};

	int i = 0;

	string res = "";

	while(num>0)
	{
		int k = num/values[i];
		for(int j=0;j<k;j++)
		{
			res += symbols[i];
			num -= values[i];
		}
		i++;
	}
	return res;



}

int main()
{
	auto start = system_clock::now();
	int num = 1;
	string res = intToRoman(num);
	cout<<res<<endl;
	auto end   = system_clock::now();
	auto duration = duration_cast<microseconds>(end - start);
	cout <<  "花费了" 
     << double(duration.count()) * microseconds::period::num / microseconds::period::den 
     << "秒" << endl;
	return 0;
}