
#one liners 

def isSameTree(self,p,q): 
   #if both not None 
   if p and q: 
       return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right) 
    
    # is key word checks if both refer to the same object 
    # if both are None, returns true 
    # if one is not None, returns false 
    return p is q  
