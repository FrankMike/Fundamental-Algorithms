class Node:
    def __init__(self, item) -> None:
        self.left = None
        self.right = None
        self.val = item

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val) + "->", end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(str(root.val) + "->", end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) + "->", end=' ')