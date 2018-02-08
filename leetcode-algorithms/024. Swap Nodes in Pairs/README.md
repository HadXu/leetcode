# Swap Nodes in Pairs

这道题目有点难度，在于对指针的运用有点乱。

**首先定义一个dummy节点，next指向head**

```cpp
ListNode dummy(0);
dummy.next = head;
ListNode *curr = &dummy;

while(curr->next && curr->next->next)
{
	ListNode* first = curr->next;
	ListNode* second = curr->next->next;
	first->next = second->next;
	curr->next = second;
	curr->next->next = first;
	curr = curr->next->next;
}
return dummy.next;
```

Python的解法是一样的。