from collections import deque


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
        #if the value is less than the current node, put it in the left node by recursively calling the func with the left child of the current Node
        if val < root.val:
            root.left = self.insert(root.left, val)
        #if the value is greater than the current node, put it in the right node by recursively calling the func with the right child of the current Node
        elif val > root.val:
            root.right = self.insert(root.right, val)
        #return the root node when we are done. This returns the completed binary search tree
        return root
    

    def minValueNode(self, root):
        #intiliaze the current to take the root node
        current = root
        #loop through the leftmost nodes, till we get the smallest node (recall l<c<r)
        while current and current.left:
            current  = current.left
        #return the smallest node, which would be the leftmost node
        return current
    def remove(self, root, val):
        #if we have no value in our tree, return None
        if not root:
            return None
        #Recursively call the function on the right most substree if the target is greater than the curr node
        if val > root.val:
            root.right = self.remove(root.right, val)
        #recursively call the function of the left subtree if the target is less than the curr node
        elif val < root.val:
            root.left = self.remove(root.left, val)
        #if target == curr node
        else:
            #replace with the left child if there is no right child
            if not root.right:
                return root.left
            #replace with the right child if there is no left child
            elif not root.left:
                return root.right
            #if node has both left and right children
            else:
                #get the leftmode node of the right subtree
                minNode = self.minValueNode(root.right)
                #replace the target node with it's inorder successor(because the successor will be greater that all the nodes in the left subtree)
                root.val = minNode.val
                #after we copy the successors value, we have to remove the original node to avoid duplication
                root.right = self.remove(root.right,minNode.val )
        return root

    #Depth First Search
    def inorder(self, root):
        if not root:
            return 
        self.inorder(root.left)
        print(root.val) #alway print the root.val
        self.inorder(root.right)
    
    def preorder(self, root):
        if not root:
            return
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)


    def postorder(self, root):
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val)

    #Breadth First Search

    def bfs(root):
        queue = deque()

        if root:
            queue.append(root)

        level = 0
        while len(queue) > 0:
            print("level: ", level)
            for i in range(len(queue)):
                curr = queue.popleft()
                print(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1
        


