class Node(object):
  def __init__(self, value):
    self.value = value
    self.right = None
    self.left = None

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
    /   \    \
   3     2    8
'''
tree = Node(5)
tree.left = Node(4)
tree.right = Node(6)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right.right = Node(8)

iterativePreorderTraversal(tree)
