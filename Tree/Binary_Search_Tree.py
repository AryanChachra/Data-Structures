class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

def preorder(root):
    if root is None:
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")

def insertnode(root, data):
    temp = node(data)
    if root is None:
        return temp
   
    parent = None
    curr = root
    while curr is not None:
        parent = curr
        if curr.data > data:
            curr = curr.left
        elif curr.data < data:
            curr = curr.right
        else:
            return root
    
    if parent.data > data:
        parent.left = temp
    else:
        parent.right = temp
    return root

def deletenode(root, data):
    curr = root
    prev = None

    while curr is not None and curr.data != data:
        prev = curr
        if curr.data < data:
            curr = curr.right
        else:
            curr = curr.left

    if curr is None:
        return root

    if curr.left is None and curr.right is None:
        if prev is None:
            return None
        if prev.left == curr:
            prev.left = None
        else:
            prev.right = None

    elif curr.left is None or curr.right is None:
        new_curr = curr.left if curr.left else curr.right
        if prev is None:
            return new_curr
        if prev.left == curr:
            prev.left = new_curr
        else:
            prev.right = new_curr

    else:
        p = None
        temp = curr.right
        while temp.left is not None:
            p = temp
            temp = temp.left

        curr.data = temp.data

        if p is not None:
            p.left = temp.right
        else:
            curr.right = temp.right
    
    return root
    
def searchnode(root, data):
    curr = root
    
    while curr is not None:
        if curr.data == data:
            return True
        elif curr.data < data:
            curr = curr.right
        else:
            curr = curr.left
    return False

def main():
    root = None
    n = int(input())
    for i in range(n):
        val = input()
        root = insertnode(root,val)
    
    print("InOrder Traversal:", end=" ")
    inorder(root)
    print("\nPreOrder Traversal:", end=" ")
    preorder(root)
    print("\nPostOrder Traversal:", end=" ")
    postorder(root)
    print("\n")

    m = int(input())
    for j in range(m):
        val = input()
        root = deletenode(root, val)
    
    print("InOrder Traversal:", end=" ")
    inorder(root)
    print("\nPreOrder Traversal:", end=" ")
    preorder(root)
    print("\nPostOrder Traversal:", end=" ")
    postorder(root)
    print("\n")

    val = input()
    print("Found" if searchnode(root, val) else "Not Found")
    
if  __name__ == "__main__":
    main()
