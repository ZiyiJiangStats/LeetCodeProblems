class Solution: 
    def isSameTree(self,p,q): 
    
        # check if nodes are empty then compare the value of the nodes 
        # then recursively check the left child and right child
        if not p and not q: 
            return True

        if not q or not p: 
            return False 
         
        if p.val != q.val: 
            return False 
        
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left,q.left) 
