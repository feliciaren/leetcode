#include<vector>
#include<iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

void show_l(ListNode* head){
    while(head){
        cout<<head->val<<" ";
        head = head->next;
    }
    cout<<endl;
}

void reorderList(ListNode* head) {
    if(!head||!head->next) return;
    ListNode* fast = head,*slow = head,*pre=NULL,*cur;
    while(fast->next and fast->next->next){
        slow = slow->next;
        fast = fast->next->next;
    }
    fast = slow->next;
    slow->next = NULL;
    while(fast){
        cur = fast->next;
        fast->next = pre;
        pre = fast;
        fast = cur;
    }
    slow = head;
    fast = pre;
    while(slow and fast){
        cur = fast;
        fast = fast->next;
        cur->next = slow->next;
        slow->next = cur;
        slow = cur->next;
    }
}

int main(){
    cout<<"Lists Length: "<<endl;
    int k,t;
    cin>>k;
    ListNode* dummy = new ListNode(0),*cur = dummy;
    for(int i = 0;i<k;i++){
        cin>>t;
        ListNode* tmp = new ListNode(t);
        cur->next = tmp;
        cur = cur->next;
    }
    cout<<"Input List:"<<endl;
    show_l(dummy->next);
    reorderList(dummy->next);
    cout<<"Result List:"<<endl;
    show_l(dummy->next);
}