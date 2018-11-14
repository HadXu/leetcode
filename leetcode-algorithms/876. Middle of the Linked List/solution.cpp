class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode *fast,*slow;
        fast = head;
        slow = head;

        while(fast->next && fast->next->next){
            fast = fast->next->next;
            slow = slow->next;
        }

        if(fast->next)
            slow = slow->next;
        return slow;
    }
};