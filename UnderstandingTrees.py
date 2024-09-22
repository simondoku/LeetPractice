class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

#searching a binary search tree 
#Time Complexity O(logn)
def search(root, target):
    if not root:
        return False
    if target > root.val:
        return search(root.right, target)
    elif target < root.val:
        return search(root.left, target)
    else:
        return True

 #time complexity O(logn)  if balanced  
def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root

#Time Complexity O(logn) if balanced O(n) if unbalanced
#Space Complexity O(logn) best Case O(n) worst case

def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr
def remove(root, val):
    if not root:
        return None
    
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    return root

#Depth First Search

#Inorder Traversal
#Prints nodes in sorted order if it's a binary tree
def inOrder(root):
    if not root:
        return None
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)

#Preorder Traversal
def preorder(root):
    if not root:
        return None
    print(root.val)
    preorder(root.left)
    preorder(root.right)

#Postorder Traversal

def postorder(root):
    if not root:
        return None
    postorder(root.left)
    postorder(root.right)
    print(root.val)