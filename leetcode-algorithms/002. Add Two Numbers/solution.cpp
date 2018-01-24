#include <iostream>
using namespace std;

struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    	ListNode dummy(-1);
    	int carry = 0;
    	ListNode *prev = &dummy;
    	for(ListNode *pa = l1,*pb = l2;pa!=nullptr || pb!=nullptr; 
    		pa = pa==nullptr?nullptr:pa->next,
    		pb = pb==nullptr?nullptr:pb->next,
    		prev = prev->next)
    	{
    		const int ai = pa==nullptr?0:pa->val;
    		const int bi = pb==nullptr?0:pb->val;
    		const int value = (ai+bi+carry)%10;
    		carry = (ai+bi+carry)/10;
    		prev->next = new ListNode(value);
    	}
    	if (carry>0)
    		prev->next = new ListNode(carry);
    	return dummy.next;
    }
};



int main()
{
	Solution s;
	ListNode *l1 = new ListNode(2);
	ListNode *l2 = new ListNode(5);
	l1->next = l2;
	ListNode *l3 = new ListNode(3);
	l2->next = l3;
	ListNode *res = s.addTwoNumbers(l1,l1);
	for(ListNode *p=res;p!=nullptr;p=p->next)
		cout<<p->val<<endl;


}