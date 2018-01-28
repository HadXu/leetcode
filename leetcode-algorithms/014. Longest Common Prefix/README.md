# 14. Longest Common Prefix

> 这一题还是很简单的，主要思想还是首先排序，然后对前后两个字符串进行比较

### C++排序

```
sort(strs.begin(),strs.end());
```

### Pyton排序

```
strs = sorted(strs)
```

```
for i in range(min(len(strs[0]),len(strs[-1]))):
	if strs[0][i] != strs[-1][i]:
		break
	res += strs[0][i]
```