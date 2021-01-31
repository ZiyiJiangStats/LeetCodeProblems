class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isValidNode(root,float('-inf'), float('inf'))
    
    def isValidNode(self, root, minVal, maxVal):
        if not root:
            return True
        return minVal<root.val<maxVal and self.isValidNode(root.left, minVal, root.val) and self.isValidNode(root.right, root.val, maxVal)
    
    
    #-inf is l which is the smallest possible value 
    # inf is r which is the largest possible value  
    
    # we want to make sure that     -inf < root.val < inf ,    -inf < root.left.val < root.val  ,  root.val < root.right.val < inf 
