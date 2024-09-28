class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

def insert_at_begin(head, data):
    new_node= node(data)
    new_node.next=head
    if head is not None:
        head.prev = new_node
    head=new_node
    return new_node

def insert_at_end(head, data):
    new_node=node(data)
    
    if head is None:
        head=new_node
    else:
        curr=head
        while curr.next is not None:
            curr=curr.next
        curr.next=new_node
        new_node.prev=curr
    return head

def insert_at_index(head,pos,data):
    new_node = node(data)
    if pos<1:
        return head
    
    if pos==1:
        insert_at_begin(head,data)
    curr = head
    for i in range(1,pos-1):
        if curr is None:
            return head
        curr = curr.next
    if curr is None:
        return head
    new_node.prev=curr
    new_node.next = curr.next
    curr.next = new_node
    if new_node.next is not None:
        new_node.next.prev = new_node
    return head
    
def forward_traversal(head):
    curr=head
    while curr is not None:
        print(curr.data)
        tail=curr
        curr=curr.next
    print()
    return tail

def backward_traversal(tail):
    curr=tail
    while curr is not None:
        print(curr.data)
        curr=curr.prev
    print()

def main():
    head=None
    n=int(input('Enter the number of Nodes to Insert: '))
    for i in range(n):
        val = int(input(f'Enter the value of the node {i+1}:'))
        head = insert_at_begin(head,val)
    
    for j in range(n):
        val = int(input('Enter the data to be inserted at end: '))
        head=insert_at_end(head,val)
    
    pos = int(input('enter the position: '))
    val = int(input('Enter the data: '))
    head = insert_at_index(head,pos,val)
    
    print('Forward Traversal')
    tail = forward_traversal(head)

    print('Backward Traversal')
    backward_traversal(tail)

if __name__ == "__main__":
    main()