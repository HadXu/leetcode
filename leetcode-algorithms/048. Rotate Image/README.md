# Rotate Image

```
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
```

## Python解法

灵活使用Python的zip操作

```python
A[:] = zip(*A[::-1])
```


## C++

采用传统的方法来求解 

```cpp
void rotate(vector<vector<int>>& matrix) {
	reverse(matrix.begin(),matrix.end());
	for(int i=0;i<matrix.size();i++){
		for(int j=i+1;j<matrix[i].size();j++){
			swap(matrix[i][j], matrix[j][i]);
		}
	}
}
```