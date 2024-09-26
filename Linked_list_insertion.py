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

def insert_at_end(head,value):
    new_node = node(value)
    if head is None:
        return new_node
    current=head
    while current.next is not None:
        current=current.next
    current.next=new_node
    return head

def insert_at_index(head,pos,value):
    if pos<1:
        return head
    
    if pos==1:
        insert_at_begin(head,value)
    
    prev=head
    count=1
    
    while count<pos-1 and prev is not None:
        prev=prev.next
        count+=1
    
    if prev is None:
        return head
    
    new_node = node(value)
    new_node.next=prev.next
    prev.next=new_node
    return head
    

def main():
    head=None
    n=int(input())
    print('Insert at end')
    for i in range(n):
        val=input()
        head = insert_at_end(head,val)
    print('Insert at begin')
    for j in range(n):
        val=input()
        head= insert_at_begin(head,val)
    print('Insert at index')
    pos = int(input())
    val=input()
    head = insert_at_index(head,pos,val)
    
    print('Traverse')
    traverse(head)
    
if __name__ =="__main__":
    main()