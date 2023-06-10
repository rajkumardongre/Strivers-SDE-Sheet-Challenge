class Node:
    def __init__(self, val=0, next=None, child=None):
        self.data = val
        self.next = next
        self.child = child


# Don't change the code above.

def merge2LL(l1, l2):
    res = Node(0)
    temp = res
    while(l1 and l2):
        if(l1.data < l2.data):
            temp.child = l1
            temp = temp.child
            l1 = l1.child
        else:
            temp.child = l2
            temp = temp.child
            l2 = l2.child

    if(l1):
        temp.child = l1
    else:
        temp.child = l2
    return res.child 

def flattenLinkedList(head: Node) -> Node:
    if(head == None or head.next == None):
        return head
    
    head.next = flattenLinkedList(head.next)
    head = merge2LL(head, head.next)
    return head