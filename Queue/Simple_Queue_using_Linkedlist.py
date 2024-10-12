class node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def isEmpty(self):
        return self.front is None and self.rear is None
    
    def EnQueue(self,data):
        new_node = node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        
        self.rear.next = new_node
        self.rear = new_node
    
    def DeQueue(self):
        if self.isEmpty():
            return
        
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
    
    def queue_front(self):
        if self.isEmpty():
            print('Queue is Empty!!')
            return
        else:
            return self.front.data
    
    def queue_rear(self):
        if self.isEmpty():
            print('Queue is Empty!!')
            return
        else:
            return self.rear.data

def main():
    n=int(input('Enter the size of Queue: '))
    que = queue()
    for i in range(n):
        val = input('Enter the data: ')
        que.EnQueue(val)
    
    print(que.queue_front())
    print(que.queue_rear())
    que.DeQueue()
    print(que.queue_front())
    print(que.queue_rear())

if __name__ == "__main__":
    main()
