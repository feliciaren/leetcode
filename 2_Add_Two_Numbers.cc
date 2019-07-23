    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* result = new ListNode(0);
        ListNode* p1 = l1;
        ListNode* p2 = l2;
        int flag = 0;
        ListNode* pre = result;
        int val;
        while(p1 && p2){
            val = p1->val + p2->val + flag;
            ListNode* cur = new ListNode(0);
            if(val<10){
                cur->val = val;
                flag = 0;
            }
            else{
                cur-> val = val - 10;
                flag = 1;
            }
            pre->next = cur;
            pre = cur;
            p1 = p1->next;
            p2 = p2->next;
        }
        ListNode* p = p1?p1:p2;
        while(p){
            val = p->val + flag;
            ListNode* cur = new ListNode(0);
            if(val < 10){
                cur->val = val;
                flag = 0;
            }
            else{
                cur->val = val -10;
                flag = 1;
            }
            pre->next = cur;
            pre = cur;
            p = p->next;
        }
        if(flag){
            ListNode* cur = new ListNode(flag);
            pre->next = cur;
        }
        return result->next;
    }