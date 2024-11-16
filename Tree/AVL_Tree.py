class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    if not node:
        return 0
    return node.height
    
def right_rotate(y):
    x = y.left
    temp = x.right
    
    x.right = y.left
    y.left = temp
    
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))
    
    return x

def left_rotate(x):
    y = x.right
    temp = y.left
    
    y.left = x
    x.right = temp
    
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))
    
    return y

def get_balance(root):
    if not root:
        return 0
    return height(root.left) - height(root.right)

def insertnode(root, data):
    if not root:
        return node(data)
    
    if data < root.data:
        root.left = insertnode(root.left, data)
    elif data > root.data:
        root.right = insertnode(root.right, data)
    else:
        return root
    
    root.height = 1 + max(height(root.left), height(root.right))
    
    balance = get_balance(root)
    
    if balance > 1 and data < root.left.data:
        return right_rotate(root)
    
    if balance < -1 and data > root.right.data:
        return left_rotate(root)
    
    if balance > 1 and data > root.left.data:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    
    if balance < -1 and data < root.right.data:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    
    return root

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def min_value(root):
    curr = root
    
    if curr.left is not None:
        curr = curr.left
    
    return curr

def deletenode(root, data):
    if root is None:
        return root
    
    if data < root.data:
        root.left = deletenode(root.left, data)
    
    elif data > root.data:
        root.right = deletenode(root.right, data)
    
    else:
        if root.left is None or root.right is None:
            temp = root.left if root.left else root.right
            
            if temp is None:
                root = None
            else:
                root = temp
        
        else:
            temp = min_value(root.right)
            root.data = temp.data
            root.right = deletenode(root.right, temp.data)
        
    if root is None:
        return root
    
    root.height = 1 + max(height(root.left), height(root.right))
    balance = get_balance(root)
    
    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)
    
    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)
    
    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    
    return root

def searchnode(root, data):
    while root:
        if data == root.data:
            return True
        elif data < root.data:
            root = root.left
        else:
            root = root.right
    return False

def main():
    n=int(input())
    root = None
    for i in range(n):
        val = input()
        root = insertnode(root, val)
    
    preorder(root)
    print('\n')
    
    m=int(input())
    for j in range(m):
        val = input()
        root = deletenode(root, val)
    
    preorder(root)
    print('\n')
    
    val = input()
    print('True' if searchnode(root, val) else 'False')

if __name__ == "__main__":
    main()
