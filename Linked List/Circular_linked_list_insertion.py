class node:
    def __init__(self,data):
        self.data=data
        self.next = None
    
def insert_at_begin(head,data):
    new_node = node(data)
    if head is None:
        new_node.next=new_node
        return new_node
    last=head
    while last.next is not head:
        last=last.next
    new_node.next = head
    last.next = new_node
    return new_node

def insert_at_end(head,data):
    new_node=node(data)
    if head is None:
        new_node.next=new_node
        return new_node
    last=head
    while last.next is not head:
        last=last.next
    last.next=new_node
    new_node.next=head
    return head

def insert_at_index(head,pos,data):
    new_node=node(data)
    if head is None:
        new_node.next=new_node
        return new_node
    
    if pos==1:
        last = head
        while last.next is not head:
            last=last.next
        new_node.next=head
        last.next=new_node
        return new_node

    curr=head
    for i in range(1,pos-1):
        curr=curr.next
        if curr==head:
            return head
        
    if curr.next==head:
        last = head
        while last.next is not head:
            last=last.next
        last.next=new_node
        new_node.next=head
        return head
    
    new_node.next=curr.next
    curr.next=new_node
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
    head = None
    n=int(input())
    for i in range(n):
        val = int(input())
        head = insert_at_begin(head,val)

    for j in range(n):
        val = int(input())
        head = insert_at_end(head,val)
    
    traversal(head)

    pos = int(input())
    val = int(input())
    head = insert_at_index(head,pos,val)

    traversal(head)
    

if __name__ == "__main__":
    main()
