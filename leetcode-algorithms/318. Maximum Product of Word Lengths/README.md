# Maximum Product of Word Lengths

### 这个问题主要在于考虑两个字符串是否有相同的字符。

开始使用set进行判断，但是系统给出超时

### 看了下讨论里面的答案，原来采用了位运算。

**如何采用位运算**

```python
假设现在有 ae 与 rt两个字符串，将a映射为1，将b映射为2，如此类推
则 a > 1
b > 2
c > 4
d > 8
e > 16
...

则ae就为  1 | 16 = format(17,'b') = '10001'
rt = '655360'
655360 & 10001 = 0

er  = 131088
131088 & 10001 = 16 != 0
```


代码如下

```python
res = 0
cheaker = []
l = len(words)
for word in words:
	num = 0
	for c in word:
		num  |= 1<<(ord(c) - ord('a'))
	cheaker.append(num)



for i in range(0,l-1):
	for j in range(i,l):
		if (cheaker[i] & cheaker[j]) == 0:
			res = max(res, len(words[i]) * len(words[j]))

return res
```