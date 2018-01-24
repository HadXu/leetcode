# 5. Longest Palindromic Substring

> 該題目剛看的時候，有點難度，求一個字符串的最長匯文字符串

**使用的方法是扩展法。从当前的字符开始扩展，如果满足条件就分别向前向后扩展，直到不满足条件，这时求每个子串的最大值。**

求子串，C++11有这种方法。

```
string s("fasdfas");
string res = s.substr(start,start+len);
```

Python同理，但是出现问题好奇怪，在线AC与本机不一样!