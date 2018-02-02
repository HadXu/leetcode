#include <iostream>
using namespace std;
ListNode* removeNthFromEnd(ListNode* head, int n) {
	ListNode f(0);
	f.next = head;
	head = &f;

	if(head==NULL || n < 0)
		return head;
	ListNode* p1,*p2;
	p1 = p2 = head;
	for(int i=0;i<n;i++){
		if(p2==NULL)
			return NULL;
		p2 = p2->next;
	}
	while(p2->next){
		p2 = p2->next;
		p1 = p1->next;
	}
	p1->next = p1->next->next;
	return head->next;
}
int main()
{
	return 0;
}