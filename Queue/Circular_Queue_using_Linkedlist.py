class node:
    def __init__(self):
        self.data = None
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def EnQueue(self,data):
        temp=node()
        temp.data = data
        if (self.front == None):
            self.front = temp
        else:
            self.rear.next = temp
        
        self.rear = temp
        self.rear.next = self.front
    
    def DeQueue(self):
        if self.front == None:
            print('Queue is Empty!!')
        
        val = None
        if self.front == self.rear:
            val = self.front.data
            self.front = None
            self.rear = None
        else:
            temp = self.front
            val = temp.data
            self.front = self.front.next
            self.rear.next = self.front
        
        return val
    
    def Display(self):
        if self.front is None:
            print('Queue is Empty!!')

        temp = self.front
        while temp.next != self.front:
            print(temp.data, end=" ")
            temp = temp.next
        print(temp.data)


def main():
    q=Queue()
    q.EnQueue(14) 
    q.EnQueue(11) 
    q.EnQueue(25)
    q.Display()

    q.DeQueue()
    q.DeQueue()
    q.Display()
    
    q.EnQueue(21)
    q.EnQueue(10)   
    q.Display()


if __name__=="__main__":
    main()
