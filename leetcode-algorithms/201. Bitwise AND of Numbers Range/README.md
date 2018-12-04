# Bitwise AND of Numbers Range

开始直觉

```python
for x in range(m+1,n+1):
		m &= x
	return m
```

后来想想 如果m为0 则下面都是0

在仔细思考一下，只要计算左边相同的1的个数即可。