class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.root=None
    
    def isEmpty(self):
        return True if self.root is None else False
    
    def push(self,data):
        new_node=node(data)
        new_node.next=self.root
        self.root=new_node
        
    def pop(self):
        if (self.isEmpty()):
            return None
        temp=self.root
        self.root=self.root.next
        popped = temp.data
        return popped
    
    def show_top(self):
        if self.isEmpty():
            return None
        return self.root.data
    

def main():
    stack=Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)
    print(stack.show_top())
    stack.pop()
    print(stack.show_top())
    stack.pop()
    print(stack.show_top())

if __name__ == "__main__":
    main()
