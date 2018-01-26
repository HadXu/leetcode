# Integer to Roman

将数字转换为罗马数字,根据wiki的定义[Roman numerals](https://en.wikipedia.org/wiki/Roman_numerals),

```
Symbol	I	V	X	L	C	D	M
Value	1	5	10	50	100	500	1,000
```

那么在计算机中实现即用一对一的方式将分界点表达出来

```
values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
symbols = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
```


### 时间计时方法

```
#include <chrono>
using namespace chrono;
....
auto start = system_clock::now();
int num = 1;
string res = intToRoman(num);
cout<<res<<endl;
auto end   = system_clock::now();
auto duration = duration_cast<microseconds>(end - start);
cout <<  "花费了" 
 << double(duration.count()) * microseconds::period::num / microseconds::period::den 
 << "秒" << endl;
```