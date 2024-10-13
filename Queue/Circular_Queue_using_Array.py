class circular_queue():
    def __init__(self,capacity):
        self.capacity = capacity
        self.q = [None]*capacity
        self.front = self.rear = -1
    
    def EnQueue(self,data):
        if ((self.rear+1)%self.capacity == self.front):
            print('Queue is Full')
        
        elif (self.front == -1):
            self.front=0
            self.rear=0
            self.q[self.rear] = data
        
        else:
            self.rear = (self.rear+1) % self.capacity
            self.q[self.rear] = data
    
    def DeQueue(self):
        if (self.front == -1):
            print('Queue is Empty!!')
        
        elif (self.front == self.rear):
            temp=self.q[self.front]
            self.front = -1
            self.rear = -1
            return temp
        
        else:
            temp = self.q[self.front]
            self.front = (self.front +1) % self.capacity
            return temp
    
    def queue_front(self):
        print('Front data is: ', self.q[self.front])

    def queue_rear(self):
        print('Rear data is: ',self.q[self.rear])
    
    def display(self):
        if(self.front == -1): 
            print ("Queue is Empty")
 
        elif (self.rear >= self.front):
            for i in range(self.front, self.rear + 1):
                print(self.q[i], end = " ")
            print ()
 
        else:
            for i in range(self.front, self.capacity):
                print(self.q[i], end = " ")
            for i in range(0, self.rear + 1):
                print(self.q[i], end = " ")
            print ()
        
        if ((self.rear + 1) % self.capacity == self.front):
            print("Queue is Full")

# main function for elif part to work in display function
# def main():
#     n=int(input('Enter the size of the Queue: '))
#     q=circular_queue(n)
#     for i in range(n):
#         val=input('Enter the data: ')
#         q.EnQueue(val)
    
#     q.display()
#     q.queue_front()
#     q.queue_rear()
#     q.DeQueue()
#     q.queue_front()
#     q.queue_rear()
#     q.display()

# main function for else part to work in display function (rear wraps around to the beginning)
def main():
    n = int(input('Enter the size of the Queue: '))
    q = circular_queue(n)

    q.EnQueue(1)
    q.EnQueue(2)
    q.EnQueue(3)
    q.EnQueue(4)
    q.DeQueue()
    q.DeQueue()
    q.EnQueue(5)
    q.EnQueue(6)
    q.display()
    q.queue_front()
    q.queue_rear()

if __name__ == "__main__":
    main()
