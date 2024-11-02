class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class dequeue:
    def __init__(self,size):
        self.front = None
        self.rear = None
        self.size = 0
        
    def isEmpty(self):
        return self.front==None
    
   
    
    def insertatfront(self,data):
        new_node = node(data)
        
        if self.front == None:
            self.rear = new_node
            self.front = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        
        self.size += 1
    
    def insertatrear(self,data):
        new_node = node(data)

        if(self.rear == None):
            self.front = new_node
            self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1
        
    
    def deleteatfront(self):
        if (self.isEmpty()):
            print('Empty')
            return
        
        temp = self.front
        self.front = self.front.next
        if (self.front == None):
            self.rear = None
        else:
            self.front.prev = None
        
        self.size -= 1
    
    def deletearrear(self):
        if (self.isEmpty()):
            print('Empty')
            return
        
        temp = self.rear
        self.rear = self.rear.prev
        if (self.rear == None):
            self.front = None
        else:
            self.rear.next = None
        
        self.size -= 1
    
    def getFront(self):
        if (self.isEmpty()):
            print('Empty')
            return
        return self.front.data
    
    def getRear(self):
        if(self.isEmpty()):
            print('Empty')
            return
        return self.rear.data
    
    def displayfromfront(self):
        if(self.isEmpty()):
            print('Empty')
            return
        
        curr = self.front
        while curr:
            print(curr.data, end = ' ')
            curr = curr.next
        
    
    def displayfromrear(self):
        if(self.isEmpty()):
            print('Empty')
            return
        
        curr = self.rear
        while curr:
            print(curr.data, end = ' ')
            curr = curr.prev


def main():
    m=int(input('Size of Queue: '))
    q=dequeue(m)
    
    for i in range(m//2):
        val=input()
        q.insertatfront(val)
    
    for j in range(m//2):
        val=input()
        q.insertatrear(val)

    print('Front')
    print(q.getFront())
    print('Rear')
    print(q.getRear())
    print('Display from front to rear')
    q.displayfromfront()
    print('\nDisplay from rear to front')
    q.displayfromrear()
    
    q.deleteatfront()
    q.deletearrear()
    
    print('\nFront')
    print(q.getFront())
    print('Rear')
    print(q.getRear())
    print('Display from front to rear')
    q.displayfromfront()
    print('\nDisplay from rear to front')
    q.displayfromrear()
    
    
if __name__ == "__main__":
    main()
