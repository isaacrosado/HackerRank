""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def getLargestKeyInTree(node):
    if node.left == None and node.right == None:
        return node.data
    elif node.left == None:
        return max(node.data, getLargestKeyInTree(node.right))
    elif node.right == None:
        return max(node.data, getLargestKeyInTree(node.left))
    else:
        return max(node.data, getLargestKeyInTree(node.left), getLargestKeyInTree(node.right))


def getSmallestKeyInTree(node):
    if node.right == None and node.left == None:
        return node.data
    elif node.left == None:
        return min(node.data, getSmallestKeyInTree(node.right))
    elif node.right == None:
        return min(node.data, getSmallestKeyInTree(node.left))
    else:
        return min(node.data, getSmallestKeyInTree(node.left), getSmallestKeyInTree(node.right))


def checkBST(root):
    if root.left == None and root.right == None:
        return True
    elif root.left == None:
        return root.data < getSmallestKeyInTree(root.right) and checkBST(root.right)
    elif root.right == None:
        return root.data > getLargestKeyInTree(root.left) and checkBST(root.left)
    else:
        return root.data < getSmallestKeyInTree(root.right) and checkBST(root.right) \
               and root.data > getLargestKeyInTree(root.left) and checkBST(root.left)


