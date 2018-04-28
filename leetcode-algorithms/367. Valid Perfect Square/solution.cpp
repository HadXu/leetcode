#include <iostream>





bool isPerfectSquare(int num) {
	int i=1;
	while(num>0){
		num -= i;
		i += 2;
	}
	return num == 0;
}

int main()
{
	int num = 14;
	std::cout<<isPerfectSquare(num)<<std::endl;
	return 0;
}