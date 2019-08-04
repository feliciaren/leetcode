class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if(!head || !head->next) return head; 
        ListNode* pre = head,*cur = head->next;
        while(cur and cur->next){
            ListNode* temp = pre->next;
            pre->next = cur->next;
            cur->next = cur->next->next;
            pre->next->next = temp;
            pre = pre->next;
            cur = cur->next;
        }
        return head;
    }
};