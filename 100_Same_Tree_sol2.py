
#use deque 
#start from the root. Each time pop the current node out of deque 

from collections import deque 

class Solution: 
  def isSameTree(self,p,q): 
    #append the root as a two tuple 
    deq = deque([(p,q),])
    
    #helper function check(p,q) 
    def check(p,q): 
      if not p and not q: 
        return True
      if not q or not p: 
        return False 
      if p.val!=q.val: 
        return False 
      return True 
    
    while deq: 
      p,q = deq.popleft() 
      
      #check whether two trees are equal at this node with the helper function 
      if not check(p,q):
        return False 
       
      #if yes, then proceed to append left child and right child to the deque 
      if p:  
        deq.append(p.left,q.left)
        deq.append(p.right,q.right)
       
      return True 
