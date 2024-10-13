class node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None
    

class Queue:
    def __init__(self):
        self.front = None
    
    def isEmpty(self):
        return True if self.front == None else False
    
    def EnQueue(self, data, priority):
        if self.isEmpty() == True:
            self.front = node(data, priority)
            return
        else:
            if self.front.priority < priority:
                new_node = node(data, priority)
                new_node.next = self.front
                self.front = new_node
                return
            else:
                temp = self.front
                while temp.next:
                    if priority >= temp.next.priority:
                        break
                    temp = temp.next
                
                new_node = node(data, priority)
                new_node.next = temp.next
                temp.next = new_node
                return
    
    def DeQueue(self):
        if self.isEmpty() == True:
            return
        else:
            self.front = self.front.next
            return
    
    def peek(self):
        if self.isEmpty() == True:
            print('Queue is Empty!!')
            return
        else:
            return self.front.data
    
    def traverse(self):
        if self.isEmpty() == True:
            print('Queue is Empty!!')
            return
        else:
            temp = self.front
            while temp:
                print(temp.data, end=" ")
                temp = temp.next

def main():
    q = Queue()
    q.EnQueue(12,2)
    q.EnQueue(14,8)
    q.EnQueue(16,6)
    q.EnQueue(18,4)
    q.EnQueue(10,2)
    q.traverse()

    print('\n')
    q.DeQueue()
    q.traverse()


if __name__ == "__main__":
    main()
