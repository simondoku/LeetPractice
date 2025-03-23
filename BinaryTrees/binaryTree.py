class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None
    #This is a binary tree that is sorted. The left < curr < right
    def binarySearchTree(self, root, target):
        if not root:
            return False
        if target > root.val:
            return self.binarySearchTree(root.right, target)
        elif target < root.val:
            return self.binarySearchTree(root.left, target)
        else:
            return True
