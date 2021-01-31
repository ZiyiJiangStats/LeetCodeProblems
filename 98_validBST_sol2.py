class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isValidNode(root,float('-inf'), float('inf'))
    
    def isValidNode(self, root, l, r):
        if not root:
            return True
        return l<root.val<r and self.isValidNode(root.left, l, root.val) and self.isValidNode(root.right, root.val, r)
    
    
    #-inf is l which is the smallest possible value 
    # inf is r which is the largest possible value  
    
    # we want to make sure that     -inf < root.val < inf ,    -inf < root.left.val < root.val  ,  root.val < root.right.val < inf 
