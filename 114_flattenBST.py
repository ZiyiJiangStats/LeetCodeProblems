

#in order traversal 

class Solution:
# @param root, a tree node
# @return nothing, do it in place
prev = None
def flatten(self, root):
    if not root:
        return
    self.prev = root
    self.flatten(root.left)

    temp = root.right
    root.right, root.left = root.left, None
    self.prev.right = temp

    self.flatten(temp)
