#include <bits/stdc++.h> 
/****************************************************************

    Following is the class structure of the LinkedListNode class:

    template <typename T>
    class LinkedListNode
    {
    public:
        T data;
        LinkedListNode<T> *next;
        LinkedListNode(T data)
        {
            this->data = data;
            this->next = NULL;
        }
    };

*****************************************************************/
LinkedListNode<int>* revPtr(LinkedListNode<int> *head){
    LinkedListNode<int> *prev=NULL,*curr=head, *next=NULL;
    if(head==NULL) return NULL;
    next = head->next;
    while(curr != NULL){
        curr->next = prev;
        prev = curr;
        curr = next;
        if(next) next = next->next;
    } 
    return prev;
}

LinkedListNode<int>* middle(LinkedListNode<int> *head){
    LinkedListNode<int> *slow=head, *fast=head;
    while(fast->next && fast->next->next){
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}


bool isPalindrome(LinkedListNode<int> *head) {
    if(head == NULL || head->next==NULL){
        return true;
    }
    // bool ans;
    LinkedListNode<int> *mid = middle(head);
    mid->next = revPtr(mid->next);
    LinkedListNode<int> *s1 = head, *s2=mid->next;
    while (s2) {
        if(s1->data != s2->data)return false;
        s1 = s1->next;
        s2 = s2->next;
    }
    return true;
}