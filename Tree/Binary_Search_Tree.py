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

def deletenode(root,data):
    curr = root
    prev = None

    while (curr != None and curr.data != data):
        prev = curr
        if curr.data < data:
            curr = curr.right
        else:
            curr = curr.left
    
    if curr == None:
        return root
    
    if curr.left == None or curr.right == None:
        newCurr = None
        if curr.left == prev.left:
            newCurr = curr.right
        else:
            newCurr = curr.left
    
        if prev == None:
            return newCurr
    
        if curr == prev.left:
            prev.left = newCurr
        else:
            prev.right == newCurr
    
        curr = None
    
    else:
        p = None
        temp = None

        temp = curr.right
        while(temp.left != None):
            p = temp
            temp = temp.left
        
        if p != None:
            p.left = temp.right
        else:
            curr.right = temp.right
        curr.data = temp.data
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
        val = int(input())
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