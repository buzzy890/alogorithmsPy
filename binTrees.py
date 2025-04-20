import math

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def printTree(tree:TreeNode, message="root"):
    print(f"{message} {tree.key}")
    if(tree.left != None):
        printTree(tree.left, "left")
    if(tree.right!=None):
        printTree(tree.right, "right")

def parse_tree(data):
    if (isinstance(data,tuple) and len(data)==3):
        node = TreeNode(data[1])
        node.left=parse_tree(data[0])
        node.right=parse_tree(data[2])
    elif (data==None):
        node=None
    else:
        node = TreeNode(data)
    return node

node0 = TreeNode(2)
node1 = TreeNode(3)
node2 = TreeNode(5)
node3 = TreeNode(1)
node4 = TreeNode(3)
node5 = TreeNode(7)
node6=TreeNode(4)
node7=TreeNode(6)
node8=TreeNode(8)
node0.left=node1
node0.right=node2
node1.left=node3
node2.left=node4
node2.right=node5
node4.right=node6
node5.left=node7
node5.right=node8

tree = node0
printTree(tree)

tree_tuple = ((1,3,None),2,((None,3,4),5,(6,7,8)))
print(tree_tuple)

def treeToTuple(node:TreeNode):
    list = [None, None, None]
    list[1] = node.key
    if node.left:
        list[0] = treeToTuple(node.left)
    else:
        list[0] = None
    if node.right:
        list[2] = treeToTuple(node.right)
    else:
        list[2] = None
    return list


tree2 = parse_tree(tree_tuple)
printTree(tree2)
print(treeToTuple(tree2))