/****************************************************************

    Following is the class structure of the Node class:

        class Node
        {
        public:
            int data;
            Node *next;
            Node()
            {
                this->data = 0;
                next = NULL;
            }
            Node(int data)
            {
                this->data = data;
                this->next = NULL;
            }
            Node(int data, Node* next)
            {
                this->data = data;
                this->next = next;
            }
        };

*****************************************************************/
int len(Node *head){
    int n = 0;
    Node *temp = head;
    while(temp!=NULL){
        n++;
        temp = temp->next;
    }
    return n;
}

Node* findIntersection(Node *firstHead, Node *secondHead)
{
    int l1 = len(firstHead);
    int l2 = len(secondHead);
    int s = 0;
    Node *p1 = NULL;
    Node *p2 = NULL;
    if(l1 > l2){
        s = l1 - l2;
        p1 = firstHead;
        p2 = secondHead;
    }else{
        s = l2 - l1;
        p1 = secondHead;
        p2 = firstHead;
    }
    while(s != 0){
        p1 = p1->next;
        s--;
    }
    while(p1!=NULL && p2!=NULL){
        if(p1 == p2){
            return p1;
        }
        p1 = p1->next;
        p2 = p2->next;
    }
    return NULL;
}