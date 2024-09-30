class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def insert_at_begin(head,data):
    new_node=node(data)
    if head is None:
        new_node.next=new_node
        return new_node
    last=head
    while last.next is not head:
        last=last.next
    new_node.next=head
    last.next=new_node
    return new_node
    
def delete_at_begin(head):
    if head is None:
        return None
    curr=head
    if curr.next==head:
        return None
    last = head
    while last.next is not head:
        last=last.next
    head=curr.next
    last.next=head
    return head
    
def delete_at_end(head):
    if head is None:
        return None
    curr=head
    if curr.next==head:
        return None
    while curr.next.next is not head:
        curr=curr.next
    curr.next=head
    return head

def delete_at_index(head,pos):
    if head is None:
        return None
    if pos<1:
        return None
    if pos==1:
        curr=head
        if curr.next==head:
            return None
        last=head
        while last.next is not head:
            last=last.next
        head=curr.next
        last.next=head
        return head
    temp1=head
    temp2=head.next
    for i in range(1,pos-1):
        temp1=temp1.next
        temp2=temp2.next
    if temp2.next==head:
        temp1.next=head
    else:
        temp1.next=temp2.next
    return head
    
        
    
def traversal(head):
    if head is None:
        return
    curr=head
    while True:
        print(curr.data)
        curr=curr.next
        if curr == head:
            break
    print()
    
def main():
    head=None
    n=int(input())
    for i in range(n):
        val=int(input())
        head = insert_at_begin(head,val)
    traversal(head)
    
    d=int(input())
    for j in range(d):
        head=delete_at_begin(head)
    traversal(head)
    
    for k in range(d):
        head=delete_at_end(head)
    traversal(head)
    
    pos=int(input())
    head = delete_at_index(head,pos)
    traversal(head)

if __name__=="__main__":
    main()
