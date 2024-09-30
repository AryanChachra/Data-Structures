class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def insert_at_begin(head,data):
    new_node = node(data)
    if head is None:
        new_node.next = new_node.prev = new_node
        return new_node
    
    last = head.prev
    new_node.next = head
    new_node.prev=last
    head.prev = new_node
    last.next = new_node
    return new_node

def delete_at_begin(head):
    if head is None:
        return None
    
    if head.next == head:
        return None
    
    last = head.prev
    head = head.next
    last.next = head
    head.prev = last 
    return head

def delete_at_end(head):
    if head is None:
        return None
    
    if head.next == head:
        return None
        
    last = head.prev
    last.prev.next=head
    head.prev=last.prev
    return head

def delete_at_index(head,pos):
    if pos<1:
        return None
        
    if head is None:
        return None
    
    if head.next is None:
        return None
        
    if pos==1:
        last=head.prev
        head=head.next
        last.next=head
        head.prev=last
        return head
        
    curr=head
    for i in range(1,pos):
        curr = curr.next
    
    if curr.next==head:
        last=head.prev
        last.prev.next=head
        head.prev=last.prev
    else:
        curr.prev.next=curr.next
        curr.next.prev=curr.prev
    return head

def traversal(head):
    if head is None:
        return None
    curr = head
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
        val = input()
        head = insert_at_begin(head,val)

    traversal(head)
    
    d=int(input())
    for j in range(d):
        head = delete_at_begin(head)

    traversal(head)
    
    for k in range(d):
        head = delete_at_end(head)
    
    traversal(head)
    
    pos = int(input())
    head = delete_at_index(head,pos)
    
    traversal(head)
    
if __name__=="__main__":
    main()