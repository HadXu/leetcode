#  Reverse Nodes in k-Group

**这道题目属于非常难的一道题目，基本思想就是每隔k个就进行小的翻转**

```cpp
ListNode *reverseOneGroup(ListNode* pre, ListNode* next)
{
	ListNode* last = pre->next;
	ListNode* cur = last->next;
	while(cur!=next)
	{
		last->next = cur->next;
		cur->next = pre->next;
		pre->next = cur;
		cur = last->next;
	}
	return last;
}
```

```cpp
ListNode* reverseKGroup(ListNode* head, int k) {
	if (!head || k == 1) return head;
	ListNode dummy(0);
	ListNode* pre = &dummy, *cur= head;
	dummy.next = head;
	int i = 0;
	while(cur)
	{
		++i;
		if(i%k==0)
		{
			pre = reverseOneGroup(pre, cur->next);
			cur = cur->next;
		}
		else
		{
			cur = cur->next;
		}
	}
	return dummy.next;
}
```




## Python没有写出来


