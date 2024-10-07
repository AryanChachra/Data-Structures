from sys import maxsize

def create_stack():
    stack=[]
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack,item):
    stack.append(item)

def pop(stack):
    if(isEmpty(stack)):
        return str(-maxsize -1)
    return stack.pop()

def show_top(stack):
    if(isEmpty(stack)):
        return str(-maxsize -1)
    return stack[len(stack)-1]

def main():
    stack = create_stack()
    push(stack,str(10))
    push(stack,str(20))
    push(stack,str(30))
    push(stack,str(40))
    top=show_top(stack)
    print(top)
    pop(stack)
    top=show_top(stack)
    print(top)

if __name__=="__main__":
    main()
