class node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data

#dfs
def in_order(root):
    
    if root is None:
        return
    in_order(root.left)
    print(root.data, end=' ')
    in_order(root.right)

def pre_order(root):
    if root is None:
        return
    print(root.data, end=' ')
    pre_order(root.left)
    pre_order(root.right)

def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.data, end=' ')

#bfs
def level_order(root):
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def insert(root,value):
    if root is None:
        return node(value)
    
    queue = [root]
    
    while queue:
        temp = queue.pop(0)
        
        if temp.left is None:
            temp.left = node(value)
            break
        else:
            queue.append(temp.left)
        
        if temp.right is None:
            temp.right = node(value)
            break
        else:
            queue.append(temp.right)
    
    return root

def delete(root,data):
    if root is None:
        return
    
    queue = [root]
    target = None
    
    while queue:
        curr = queue.pop(0)
        
        if curr.data == data:
            target = curr
            break
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    
    if target is None:
        return root
    
    last_node = None
    last_parent = None
    queue = [(root,None)]
    
    while queue:
        curr, parent = queue.pop(0)
        last_node = curr
        last_parent = parent
        
        if curr.left:
            queue.append((curr.left,curr))
        if curr.right:
            queue.append((curr.right,curr))
    
    target.data = last_node.data
    
    if last_parent:
        if last_parent.left == last_node:
            last_parent.left = None
        else:
            last_parent.right = None
    else:
        return None
    return root
    
    
def main():
    root = None
    print('Insertion')
    n=int(input())
    for i in range(n):
        val = input()
        root = insert(root,val)
    
    print('In-Order Traversal')
    in_order(root)
    print('\n')
    print('Pre-Order Traversal')
    pre_order(root)
    print('\n')
    print('Post-Order Traversal')
    post_order(root)
    print('\n')
    print('Level-Order Traversal')
    level_order(root)
    print('\n')
    
    print('Deletion')
    m = int(input())
    for i in range(m):
        delval = input()
        root = delete(root,delval)
    
    print('In-Order Traversal after deletion')
    in_order(root)
    

if __name__ == '__main__':
    main()
