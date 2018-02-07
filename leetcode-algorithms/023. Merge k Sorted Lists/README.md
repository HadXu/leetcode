# Merge k Sorted Lists

这道题目是非常难的一道题目，目的是合并排序好的链表组

## Python解法

使用优先队列

```python
from queue import PriorityQueue
dummy = ListNode(None)
curr = dummy
q = PriorityQueue()

for node in lists:
	if node:
		q.put((node.val, node))

while q.qsize()>0:
	curr.next = q.get()[1]
	curr = curr.next
	if curr.next:
		q.put((curr.next.val,curr.next))
return dummy.next
```

## C++解法

首先编写另外的函数用来合并两个链表。

接下来从数组中遍历即可。