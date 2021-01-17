
#recursive approach
class Solution(object):
    def reverseList(self, head, prev=None):
        # if head is None, returns the previous item 
        # stopping condition 
        if not head:
          return prev
  
        curr, head.next = head.next, prev
        #recursively call the function itself instead of using a while loop 
        return self.reverseList(curr, head)
