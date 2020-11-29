class Node(object):
  def __init__(self, value):
    self.value = value
    self.right = None
    self.left = None
class BinaryTree(object):
  def __init__(self, root):
    self.root = Node(root)

def iterativePreorderTraversal(root):
  if root is None:
    return
  listt = []
  listt.append(root)
  while(len(listt)>0):
    node = listt.pop()
    print(node.value)
    if node.right is not None:
      listt.append(node.right)
    if node.left is not None:
      listt.append(node.left)

#Setting Up BinaryTree
'''
         5
       /   \
      4     6
    /   \     \
   3     2     8
'''
tree = BinaryTree(5)
tree.root.left = Node(4)
tree.root.right = Node(6)
tree.root.left.left = Node(3)
tree.root.left.right = Node(2)
tree.root.right.right = Node(8)

iterativePreorderTraversal(tree.root)
