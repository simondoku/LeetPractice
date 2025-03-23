class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None
    # This is a binary tree that is sorted. The left < curr < right
    def binarySearchTree(self, root, target):
        if not root:
            return False
        if target > root.val:
            return self.binarySearchTree(root.right, target)
        elif target < root.val:
            return self.binarySearchTree(root.left, target)
        else:
            return True
    # To insert a new node into a BST, we must ensure that we maintain the l<c<r property.
    def insert(self, root, val):
        #If the tree is empty, insert the value as the first value of the tree(root)
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root