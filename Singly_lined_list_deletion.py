class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def insert_at_begin(head, value):
    new_node=node(value)
    new_node.next = head
    head=new_node
    return head

def traverse(head):
    current=head
    while current is not None:
        print('Current Data:' , current.data)
        current = current.next
    print()
    
def delete_at_begin(head):
    if not head:
        return None
    temp = head
    head=head.next
    temp=None
    return head

def delete_at_end(head):
    if head is None:
        return None
    if head.next is None:
        head=None
        return None
    second_last=head
    while second_last.next.next is not None:
        second_last=second_last.next
    second_last.next=None
    return head

def delete_at_index(head,pos):
    if head is None or pos<1:
        return head
    if pos==1:
        temp=head
        head=head.next
        temp=None
        return head
    current = head
    for i in range(1,pos-1):
        if current is not None:
            current=current.next
    if current is None or current.next is None:
        return head
    temp=current.next
    current.next=current.next.next
    temp=None
    return head
    
def main():
    head=None
    n=int(input())
    print('Insert at begin')
    for j in range(n):
        val=input()
        head= insert_at_begin(head,val)
    print('Before deletion')

    d=int(input())
    for i in range(d):
        head=delete_at_begin(head)
    
    print('After deletion at begin')
    
    for k in range(d):
        head=delete_at_end(head)
    print('After deletion at end')
    
    pos=int(input())
    head=delete_at_index(head,pos)
    traverse(head)
if __name__ =="__main__":
    main()