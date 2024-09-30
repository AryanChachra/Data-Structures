class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    
def insert_at_begin(head,data):
    new_node=node(data)
    if head is None:
        new_node.next = new_node.prev = new_node
        return new_node

    last=head.prev
    new_node.next=head
    new_node.prev=last
    head.prev=new_node
    last.next=new_node
    return new_node

def insert_at_end(head,data):
    new_node=node(data)
    if head is None:
        new_node.next = new_node.prev = new_node
        return new_node

    last=head.prev
    new_node.next=head
    new_node.prev=last
    last.next=new_node
    head.prev=new_node
    return new_node

def insert_at_index(head,pos,data):
    new_node = node(data)
    if pos<1:
        return None
    if head is None:
        new_node.next = new_node.prev = new_node
        return new_node
    if pos==1:
        last=head.prev
        new_node.next=head
        new_node.prev=last
        head.prev=new_node
        last.next=new_node
        return new_node
    
    curr=head
    for i in range(1,pos-1):
        curr=curr.next
    if curr.next is head:
        last=head.prev
        new_node.next = head
        new_node.prev = last
        last.next = new_node
        head.prev = new_node
        return new_node
    else:
        new_node.next = curr.next
        new_node.prev = curr
        curr.next.prev = new_node
        curr.next = new_node
        return head
    
def forward_traversal(head):
    if head is None:
        return None
    curr=head
    while True:
        print(curr.data)
        curr=curr.next
        if curr == head:
            break
    print()
    return tail

def backward_traversal(head):
    if head is None:
        return None
    curr=head.prev
    while True:
        print(curr.data)
        curr=curr.prev
        if curr == head.prev:
            break
    print()
    

def main():
    head=None
    n=int(input())
    for i in range(n):
        val = input()
        head = insert_at_begin(head,val)
    
    for j in range(n):
        val=int(input())
        head = insert_at_end(head,val)
    
    forward_traversal(head)
    backward_traversal(head)
    
    pos=int(input())
    val=input()
    head = insert_at_index(head,pos,val)
    
    forward_traversal(head)
    backward_traversal(head)

if __name__=="__main__":
    main()
