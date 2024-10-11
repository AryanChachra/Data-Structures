class queue:
    def __init__(self,capacity):
        self.front = self.size = 0
        self.rear = capacity -1
        self.q = [None]*capacity
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity


    def isEmpty(self):
        return self.size == 0

    def EnQueue(self,data):
        if self.isFull():
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.q[self.rear] = data
        self.size = self.size+1

    def DeQueue(self):
        if self.isEmpty():
            return
        
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1

    def queue_front(self):
        if self.isEmpty():
            print('Queue is Empty!!')
        else:
            print('Front data is: ', self.q[self.front])
        
    def queue_rear(self):
        if self.isEmpty():
            print('Queue is Empty!!')
        else:
            print('Rear data is: ',self.q[self.rear])
    

def main():
    n=int(input('Enter the size of Queue: '))
    que = queue(n)
    for i in range(n):
        val=input('Enter data: ')
        que.EnQueue(val)
    
    que.queue_front()
    que.queue_rear()
    que.DeQueue()
    que.queue_front()
    que.queue_rear()

if __name__ == '__main__':
    main()
