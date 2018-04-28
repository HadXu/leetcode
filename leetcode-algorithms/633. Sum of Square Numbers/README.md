# 633. Sum of Square Numbers

首先我使用的是两层```for```循环，但是，毫无疑问，超时了。



采用set结构

```cpp
set<int> s;
for(int i=0;i<=int(sqrt(c));i++){
	s.insert(i*i);
	if(s.find(c-i*i)!=s.end())
		return true;
}
return false;
```