#include <iostream>
#include <map>
#include <string>
using namespace std;

int romanToInt(string s) {
    map<char,int> m = {
    	{'I',1},
    	{'V',5},
    	{'X',10},
    	{'L',50},
    	{'C',100},
    	{'D',500},
    	{'M',1000}
    };

    int prev = 0, res = 0;
    for(auto c:s)
    {
    	int curr = m.at(c);
    	res += (curr>prev)?(curr-2*prev):curr;
    	prev = curr;
    }
    return res;

}

int main()
{
	string s("MMMCMXCIX");
	int res = romanToInt(s);
	cout<<res<<endl;
	return 0;
}