# Letter Combinations of a Phone Number

**该题目简单，用来求解电话号码号码对应的字符的组合**

```python
if not digits:
        return []
num2abc = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno',
			'7':'pqrs','8':'tuv','9':'wxyz'}

from itertools import product

res = []
for d in digits:
	res.append(num2abc[d])

return [''.join(l) for l in product(*res)]
```

> 使用Python真的是太方便了。

```cpp
if(digits=="")
	return res;
res.push_back("");
for(int i=0;i<digits.size();i++)
{
	vector<string> tempres;
	string chars = m[digits[i]];
	for(int c=0;c<chars.size();c++)
		for(int j=0;j<res.size();j++)
			tempres.push_back(res[j]+chars[c]);
	res = tempres;
}
```


> 对每一个组合进行循环。


