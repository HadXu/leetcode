struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};


ListNode* swapPairs(ListNode* head) {
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
}