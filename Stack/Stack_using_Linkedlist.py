class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
    
    def isEmpty(self):
        return True if self.top is None else False
    
    def push(self,data):
        new_node=node(data)
        new_node.next=self.top
        self.top=new_node
        
    def pop(self):
        if (self.isEmpty()):
            return None
        temp=self.top
        self.top=self.top.next
        popped = temp.data
        return popped
    
    def show_top(self):
        if self.isEmpty():
            return None
        return self.top.data
    

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
