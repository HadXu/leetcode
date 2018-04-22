# 实现pow

Implement pow(x, n), which calculates x raised to the power n (xn).


### 比如实现2^10

可以这样

2^10 = 4^5,然后5个4相乘即可。

```python
	if n<0:
		x = 1./x
		n = -n
	pow = 1
	while n:
		if n&1:
			pow *= x
		x *= x
		n >>= 1
	return pow
```