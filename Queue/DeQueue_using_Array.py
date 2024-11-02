class dequeue:
    def __init__(self,size):
        self.arr = [0]*100
        self.front = -1
        self.rear = 0
        self.size = size
    
    def isFull(self):
        return((self.front == 0 and self.rear == self.size-1) or self.front ==self.rear+1)
    
    def isEmpty(self):
        return self.front == 0
    
    def insertatfront(self,data):
        if (self.isFull()):
            print('Full')
            return
        
        if self.front == -1:
            self.front=0
            self.rear=0
        elif self.front == 0:
            self.front = self.size - 1
        else:
            self.front = self.front-1
        self.arr[self.front] = data
    
    def insertatrear(self,data):
        if (self.isFull()):
            print('Full')
            return
        
        if self.front == -1:
            self.front=0
            self.rear=0
        elif self.rear == self.size-1:
            self.rear=0
        else:
            self.rear = self.rear+1
        self.arr[self.rear] = data
    
    def deleteatfront(self):
        if (self.isEmpty()):
            print('Empty')
            return
        
        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
        else:
            if (self.front == self.size-1):
                self.front=0
            else:
                self.front = self.front+1
    
    
    def deleteatrear(self):
        if (self.isEmpty()):
            print('Empty')
            return
        
        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
        elif(self.rear == 0):
            self.rear = self.size-1
        else:   
            self.rear = self.rear-1
    
    def getfront(self):
        if (self.isEmpty()):
            print('Empty')
            return
        return self.arr[self.front]
    
    def getrear(self):
        if (self.isEmpty()):
            print('Empty')
            return
        return self.arr[self.rear]
    
    def displayfromfront(self):
        if (self.isEmpty()):
            print('Empty')
            return
        i = self.front
        while True:
            print(self.arr[i], end =' ')
            if i == self.rear:
                break
            i = (i + 1) % self.size
        
            
    def displayfromrear(self):
        if (self.isEmpty()):
            print('Empty')
            return
        i = self.rear
        while True:
            print(self.arr[i], end = ' ')
            if i == self.front:
                break
            i = (i - 1 + self.size) % self.size
    
    
def main():
    m=int(input('Size of Queue: '))
    q = dequeue(m)
    for i in range(m//2):
        val=input()
        q.insertatfront(val)
    
    for j in range(m//2):
        val = input()
        q.insertatrear(val)
    
    print('Front')
    print(q.getfront())
    print('Rear')
    print(q.getrear())
    print('Display from front to rear')
    q.displayfromfront()
    print('\nDisplay from rear to front')
    q.displayfromrear()
    
    q.deleteatfront()
    q.deleteatrear()
    
    print('\nFront')
    print(q.getfront())
    print('Rear')
    print(q.getrear())
    print('Display from front to rear')
    q.displayfromfront()
    print('\nDisplay from rear to front')
    q.displayfromrear()


if __name__ == "__main__":
    main()
