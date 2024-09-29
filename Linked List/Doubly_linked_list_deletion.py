class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def insert_at_begin(head,data):
    new_node= node(data)
    new_node.next=head
    if head is not None:
        head.prev = new_node
    head=new_node
    return new_node

def delete_at_begin(head):
    if head is None:
        return None
    temp=head
    head=head.next
    if head is not None:
        head.prev=None
    return head

def delete_at_end(head):
    if head is None:
        return None
    if head.next is None:
        return None
    curr=head
    while curr.next is not None:
        curr=curr.next
    if curr.prev is not None:
        curr.prev.next = None
    return head

def delete_at_index(head, pos):
    if head is None:
        return head
    curr = head
    for i in range(1, pos):

        curr = curr.next
    if curr.prev is None:
        head=head.next
        if head is not None:
            head.prev=None
        return head
    if curr.next is None:
        curr.prev.next = None
        return head
    
    curr.prev.next=curr.next
    curr.next.prev = curr.prev
    
    return head

def forward_traversal(head):
    curr = head
    while curr is not None:
        print(curr.data)
        curr=curr.next
    print()

def main():
    head = None
    n=int(input())
    for i in range(n):
        val = int(input())
        head = insert_at_begin(head,val)

    forward_traversal(head)

    d = int(input())
    for j in range(d):
        head = delete_at_begin(head)
    
    forward_traversal(head)

    for k in range(d):
        head = delete_at_end(head)
    
    forward_traversal(head)

    pos = int(input())
    head = delete_at_index(head,pos)

    forward_traversal(head)


if __name__ == "__main__":
    main()
