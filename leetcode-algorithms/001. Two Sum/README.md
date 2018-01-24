# Two Sum题解

> 该题目属于简单，思想是建立一个数到索引的字典。每次将target-num与字典中比对，如果找到，就说明结果存在，直接输出即可。

注意点

```
C++11
# 查找字典使用的技巧
m.find( target-nums[i] ) == m.end()
# 遍历迭代器
for (std::vector<int>::iterator i = res.begin(); i != res.end(); ++i)
{
	cout<<*i<<endl;	
}
```

finished on 2018-01-14