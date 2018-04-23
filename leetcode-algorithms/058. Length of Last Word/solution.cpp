#include <iostream>
#include <string>

using namespace std;

int lengthOfLastWord(string s) {
	int i = s.size() - 1;
	while(s[i]==' ' && i>=0){
		i--;
	}

	int res = 0;
	while(i>=0 && s[i]!=' '){
		i--;
		res++;
	}
	return res;


}

int main()
{
	return 0;
}