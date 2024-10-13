class item:
    def __init__(self,data,priority):
        self.data = data
        self.priority = priority

class Queue:
    size = [None]*(10000)
    link = -1

    def EnQueue(data, priority):
        Queue.link+=1
        Queue.size[Queue.link] = item(data,priority)
    
    def DeQueue():
        ele = Queue.peek()
        i=ele
        while i < Queue.link:
            Queue.size[i] = Queue.size[i+1]
            i += 1
        
        Queue.link -= 1
    
    def peek():
        highestpriority = -float('inf')
        ele =-1
        i=0
        while i <= Queue.link:
            if (highestpriority == Queue.size[i].priority and ele > -1 and Queue.size[ele].data < Queue.size[i].data):
                highestpriority = Queue.size[i].priority
                ele = i
            elif highestpriority < Queue.size[i].priority:
                highestpriority = Queue.size[i].priority
                ele = i
            i+=1
        return ele

def main():
    Queue.EnQueue(10,8)
    Queue.EnQueue(14,4)
    Queue.EnQueue(16,6)
    Queue.EnQueue(12,3)

    ele = Queue.peek()
    print(Queue.size[ele].data)

    Queue.DeQueue()

    ele = Queue.peek()
    print(Queue.size[ele].data)

if __name__ == "__main__":
    main()
